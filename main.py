from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot('MedicalBot')
bot.storage.drop()

trainer = ListTrainer(bot)

trainer.train([
    "I am injured.",
    "Please elaborate on your injuries.",
    "I got injured.",
    "Please elaborate on your injuries.",
    "I am bleeding a lot.",
    "Medical Assistance has been informed of your situation. In the meantime please apply direct pressure onto the wound using a clean cloth and stay calm while you wait.",
    "I am having a headache.",
    "How would you rate your pain from 1 to 10? 1 being mild and 10 being intense."
])

trainer.train([
    "I injured my legs.",
    "How would you rate your pain from 1 to 10? 1 being mild and 10 being intense.",
    "I injured my ankles.",
    "How would you rate your pain from 1 to 10? 1 being mild and 10 being intense.",
    "I injured my arms.",
    "How would you rate your pain from 1 to 10? 1 being mild and 10 being intense.",
    "I injured my toes.",
    "How would you rate your pain from 1 to 10? 1 being mild and 10 being intense.",
    "I injured my fingers.",
    "How would you rate your pain from 1 to 10? 1 being mild and 10 being intense.",
    "I injured my head.",
    "How would you rate your pain from 1 to 10? 1 being mild and 10 being intense.",
    "I am feeling chest pains.",
    "Are you having trouble breathing?",
    "Yes",
    "Medical Assistance has been informed of your situation. You may be experiencing a heart attack. It is advisable to take an aspirin while you wait for emergency help.",
    "No",
    "You should see a doctor as soon as possible as you may be experiencing mini heart attack."
])

trainer.train([
    "1",
    "The injury should not be serious, just clean and bandage the wound and you should be fine.",
    "2",
    "The injury should not be serious, just clean and bandage the wound and you should be fine.",
    "3",
    "The injury should not be serious, just clean and bandage the wound and you should be fine.",
    "4",
    "Please see a doctor as soon as possible.",
    "5",
    "Please see a doctor as soon as possible.",
    "6",
    "Please see a doctor as soon as possible.",
    "7",
    "Medical Assistance has been informed of your situation. Please stay calm as you wait.",
    "8",
    "Medical Assistance has been informed of your situation. Please stay calm as you wait.",
    "9",
    "Medical Assistance has been informed of your situation. Please stay calm as you wait.",
    "10",
    "Medical Assistance has been informed of your situation. Please stay calm as you wait.",
])

trainer.train([
    "Thanks!",
    "You're welcome."
])

print("Welcome to Hospital Chatbot service! How may I help you?")

while True:
    message = input('You:').lower()
    if message.strip() != 'bye':
        reply = bot.get_response(message)
        print('MedicalBot:', reply)
    if message.strip() == 'bye':
        print('MedicalBot: Remember to stay safe, bye!')
        break