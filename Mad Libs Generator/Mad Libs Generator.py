def get_user_input(word_type):
    return input(f"Please enter a {word_type}: ")

def main():
    # Define the story template
    story_template = (
        "Once upon a time, in a far away [place], there lived a [adjective] [noun]. "
        "Every day, the [noun] would [verb] by the [place2]. One day, a [adjective2] [noun2] "
        "appeared and said, 'You must [verb2] the [noun3] to save the [place3].' "
        "And so, the [adjective] [noun] set off on a quest to [verb] the [noun3] and bring peace to the [place3]."
    )

    # List of placeholders and their corresponding types
    placeholders = [
        ("[place]", "place"),
        ("[adjective]", "adjective"),
        ("[noun]", "noun"),
        ("[verb]", "verb"),
        ("[place2]", "place"),
        ("[adjective2]", "adjective"),
        ("[noun2]", "noun"),
        ("[verb2]", "verb"),
        ("[noun3]", "noun"),
        ("[place3]", "place")
    ]

    # Dictionary to store user inputs
    user_inputs = {}

    # Prompt the user for each input
    for placeholder, word_type in placeholders:
        user_inputs[placeholder] = get_user_input(word_type)

    # Replace placeholders with user inputs in the story template
    final_story = story_template
    for placeholder, user_input in user_inputs.items():
        final_story = final_story.replace(placeholder, user_input)

    # Print the final story
    print("\nHere is your Mad Libs story:")
    print(final_story)

if __name__ == "__main__":
    main()
