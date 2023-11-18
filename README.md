# Autogen Character Advisors 🌟🗨️💬

Can you imagine being able to present your problem to famous TV series characters and hear their feedback? Now it's possible...

The Autogen Dialog Assistant is an innovative project that brings characters from popular culture into the realm of automated dialogue systems. By leveraging the power of Python, Autogen, and OpenAI's GPT models, this project creates a unique and interactive chat experience where users can engage with virtual representations of beloved characters like Johnny Silverhand from Cyberpunk 2077 and Michael Scott from The Office.

## Why is this Project Fun and Engaging?

1. **Unique Characters, Unique Conversations**: Chat with iconic characters, each with their own distinct personality and style.
2. **Dynamic Interactions**: Experience how different characters might react to modern-day scenarios and dilemmas.
3. **Creative Problem Solving**: Watch as these characters offer unique perspectives and solutions to problems, making for entertaining and sometimes humorous outcomes.
4. **Expandable Framework**: The project is designed to easily incorporate more characters and scenarios, providing endless possibilities for conversation and engagement.

## THIS IS THE PART OF BIGGER PICTURE

1. This repo is starting point. Here you can define character and current problem.
2. Output look like follows:
   ```[('Karolina', "Guys. Karolina here, Bo...how? What's your advice?"), ('Michael', "Oh, Karolina! ")('Karolina', 'TERMINATE')] ```
3. Paste it into my GPT's for creating story based on json above: https://chat.openai.com/g/g-LNKK6KCcR-story-teller-from-problems
4. GPT's should create downloadble JSON looking similar to this one:
   ```json [
                {
                    "name": "Narrator",
                    "message": "In the heart of Scranton, a scene unfolded among friends, each carrying their unique charm and wit."
                },
                {
                    "name": "Karolina",
                    "message": "Guys. Karolina here, Bob's assistant, greatest friend....."
                },
                {
                    "name": "Michael",
                    "message": "Oh, Karolina! First off...."
                },
                {
                    "name": "Johnny",
                    "message": "Michaeine, ...commitment."
                },
                {
                    "name": "Narrator",
                    "message": "As the conversation co... Bob."
                }
            ]```

  5. Download json file and paste to this program https://github.com/miekki-jerry/jsonToStory
     
     Output depends on your voices, you can use openai TTS.

     Here is example output: [https://github.com/miekki-jerry/jsonToStory/blob/main/example_output.mp3](https://github.com/miekki-jerry/jsonToStory/blob/main/exmple_output.mp3)
     
## Key Features

- **Character-Based Agents**: Utilizes `AssistantAgent` and `UserProxyAgent` to simulate conversations with Johnny Silverhand and Michael Scott.
- **Customizable Chat Scenarios**: Users can set up their own scenarios and watch how these characters interact and respond.
- **Message Capturing and Processing**: The system captures and processes dialogue, allowing for further analysis or transformation, such as text-to-speech processing.
- **Expandable Framework**: Easily add new characters and scenarios to diversify the chat experience.

## How it Works

1. **Setup Agents**: Characters are set up as agents with specific personalities and conversational styles.
2. **Initiate Conversations**: Users can start conversations based on predefined or custom scenarios.
3. **Interactive Dialogue**: The characters interact with each other, offering advice or opinions based on their unique personalities.

## Technologies Used

- **Python**: For overall programming and script execution.
- **Autogen**: To manage dialogue agents and group chat interactions.
- **OpenAI API**: Leveraging GPT-4 for generating character dialogues.


Embark on an unforgettable chat adventure with the Autogen Dialog Assistant, where every conversation is a journey into the world of your favorite characters! 🌟🗨️💬
