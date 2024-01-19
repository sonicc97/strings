text = """Interesting facts about the Moon.On average, the Moon moves 4cm away from the Earth every year. The highest daylight temperature of the Moon is 127 C."""

sentences = text.split('. ')
print(sentences)

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)


new = "1/7"
print("""You gonna win this {new} of this score {new} because the {ball} is here""".format(ball ="ball", new = new))


print(f'On the earth you gonna lose for about {round(100/3, 1)}%')



# Showing string with 'title'
canada = 'I love Canada and my dream is to move there!'
canada_1 = f'{canada.title()}'
print(canada_1)


# FORMAT
name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'
template = """Gravity Facts about {name}
--------------------------
Planet name: {planet}
Gravity on {name}: {gravity} m/s2"""
print(template.format(name=name, planet=planet, gravity=gravity))