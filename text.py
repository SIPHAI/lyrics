import time

# Define the lyrics as a multiline string
lyrics = """
[Verse 1]
This is the first line of the song,
And here comes the next line.

[Chorus]
This is the chorus,
Where everyone sings along.

[Verse 2]
Now we're back to another verse,
And it just keeps getting better.

[Chorus]
This is the chorus,
Where everyone sings along.
"""

# Split the lyrics into lines
lyrics_lines = lyrics.strip().split('\n')

# Display each line with a delay
for line in lyrics_lines:
    print(line)
    time.sleep(1)  # Adjust the delay as needed (e.g., 1 second)
