#Python telegram bot
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Enable logging for debugging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Data for the quiz
quiz_data = [
    {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin"], "correct": "Paris"},
    {"question": "Who wrote '1984'?", "answers": ["George Orwell", "Aldous Huxley", "J.K. Rowling"], "correct": "George Orwell"},
    {"question": "What is 2 + 2?", "answers": ["3", "4", "5"], "correct": "4"},
    {"question": "What is the largest planet in our solar system?", "answers": ["Earth", "Jupiter", "Saturn"], "correct": "Jupiter"},
    {"question": "Who painted the Mona Lisa?", "answers": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci"], "correct": "Leonardo da Vinci"},
    {"question": "What is the speed of light?", "answers": ["300,000 km/s", "150,000 km/s", "1,000,000 km/s"], "correct": "300,000 km/s"},
    {"question": "Who discovered gravity?", "answers": ["Isaac Newton", "Albert Einstein", "Galileo Galilei"], "correct": "Isaac Newton"},
    {"question": "What is the longest river in the world?", "answers": ["Amazon", "Nile", "Yangtze"], "correct": "Nile"},
    {"question": "What is the boiling point of water?", "answers": ["100°C", "90°C", "110°C"], "correct": "100°C"},
    {"question": "What is the chemical symbol for gold?", "answers": ["Au", "Ag", "Pb"], "correct": "Au"}
]

# Dictionary to store user progress and answers
user_progress = {}

# Function to start or continue the quiz
async def start_quiz(message: types.Message):
    user_id = message.from_user.id

    # Log progress for debugging
    logger.debug(f"Starting quiz for user: {user_id}")

    # Initialize user progress if not already initialized
    if user_id not in user_progress:
        logger.debug(f"Initializing progress for user: {user_id}")
        user_progress[user_id] = {
            "current_question": 0,
            "correct_answers": 0,
            "answered_questions": [],
            "last_message_id": None  # Track last message sent by the bot
        }

    # Send the first question if the user has not completed all questions
    await send_question(message, user_id)

# Function to send a question with inline buttons
async def send_question(message: types.Message, user_id: int):
    # Log progress for debugging
    logger.debug(f"Sending question to user: {user_id}")

    # Ensure user progress exists
    if user_id not in user_progress:
        logger.error(f"User {user_id} has no progress data.")
        await message.answer("Please start the quiz first by typing /start.")
        return

    current_question = user_progress[user_id]["current_question"]

    if current_question >= len(quiz_data):
        # Quiz is over, send the results and clear the progress
        correct_answers = user_progress[user_id]["correct_answers"]
        total_questions = len(quiz_data)
        answered_questions = len(user_progress[user_id]["answered_questions"])
        
        if correct_answer<6:
            result_text=f"You are a quite dumb piece of work. {correct_answers} out of 10."
        elif correct_answer=6:
            result_text=f"Congratulations on getting the Third place! {correct_answers} out of 10."
        elif correct_answer>=7 and correct_answer<=8:
            result_text=f"Congratulations on almost getting the First place!! {correct_answers} out of 10"
            result_text = f"Quiz over! You got {correct_answers} out of {total_questions} questions correct.\n" \
                f"You answered {answered_questions} questions in total!"
        
        # If the bot has already sent a message, edit it
        if user_progress[user_id]["last_message_id"]:
            # Correct argument order here (chat_id and then message_id)
            await bot.edit_message_text(result_text, chat_id=user_id, message_id=user_progress[user_id]["last_message_id"])
        else:
            sent_message = await message.answer(result_text)
            user_progress[user_id]["last_message_id"] = sent_message.message_id
        
        del user_progress[user_id]  # Clear the user's progress
        return

    question_data = quiz_data[current_question]
    question_text = question_data["question"]
    answers = question_data["answers"]

    # Create inline keyboard for answers
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=answer, callback_data=f"answer_{answer}") for answer in answers]]
    )

    # If it's the first question, send the question as a new message
    if user_progress[user_id]["last_message_id"] is None:
        sent_message = await message.answer(question_text, reply_markup=keyboard)
        user_progress[user_id]["last_message_id"] = sent_message.message_id
    else:
        # If a message was already sent, edit it to update the question and choices
        await bot.edit_message_text(question_text, chat_id=user_id, message_id=user_progress[user_id]["last_message_id"], reply_markup=keyboard)


# Handle the answer callback
@dp.callback_query()
async def handle_answer(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id

    # Log progress for debugging
    logger.debug(f"Handling answer for user {user_id}: {callback_query.data}")

    # Ensure user progress exists
    if user_id not in user_progress:
        logger.error(f"User {user_id} is not in progress. Prompting for /start.")
        await callback_query.answer("You need to start the quiz first. Type /start to begin.")
        return

    current_question = user_progress[user_id]["current_question"]
    user_answer = callback_query.data.split("_")[1]
    correct_answer = quiz_data[current_question]["correct"]

    # Check if the answer is correct
    if user_answer == correct_answer:
        user_progress[user_id]["correct_answers"] += 1

    # Record the answered question
    user_progress[user_id]["answered_questions"].append({
        "question": quiz_data[current_question]["question"],
        "answered": user_answer,
        "correct": correct_answer,
        "is_correct": user_answer == correct_answer
    })

    # Move to the next question
    user_progress[user_id]["current_question"] += 1

    # Acknowledge the answer and edit the last message to show the next question
    await callback_query.answer(f"Your answer: {user_answer} (Correct: {user_answer == correct_answer})")
    await send_question(callback_query.message, user_id)

# Command handler for the /start command to initialize or continue the quiz
@dp.message(Command('start'))
async def start(message: types.Message):
    # Log the start command
    logger.debug(f"Received /start command from user: {message.from_user.id}")
    # When the user types /start, initialize the quiz or continue it
    await start_quiz(message)

# Main function to start polling
async def main():
    logger.debug("Starting bot...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
