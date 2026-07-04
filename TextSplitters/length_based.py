from langchain_text_splitters import CharacterTextSplitter

text = """The dust on the "Main Street Oval"—which was actually just a patch of scorched earth between two grain silos—was so thick it felt like playing on the moon.

Ten-year-old Arjun didn’t mind. In his mind, the silos were the towering stands of Lord’s, and the rusty bicycle frame serving as stumps was a set of pristine white wickets.

He was the last man standing. His team, a ragtag group of kids in mismatched sandals, needed six runs off the final ball. The bowler was "Big" Vikram, a fifteen-year-old whose fastballs were whispered to break skin. Vikram stood at the end of his long run-up, polishing the ball—a tennis ball wrapped tightly in electrical tape—against his thigh.

"Last ball, Arjun," Vikram shouted, a cocky grin splitting his face. "Go home and have your milk."

Arjun gripped his bat. It wasn't willow; it was a sturdy plank of scrap wood his father had sanded down. He felt the sweat prickling his neck. He looked at the fielders—kids crouched in the dirt, ready to pounce.

Vikram charged. He was a blur of limbs and momentum. The ball left his hand like a bullet, pitching short and whistling upward toward Arjun’s ribs—a classic "chin-music" bouncer.

Time slowed. Arjun didn’t flinch."""

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=""
)

result = splitter.split_text(text)

print(type(result))
print(len(result))
print(type(result[0]))

#### we can use result same as result of document loader
