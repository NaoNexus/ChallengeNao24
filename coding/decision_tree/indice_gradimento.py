def morphcast(emozioni):
	angry = int(emozioni['angry'] * 100)
	disgust = int(emozioni['disgust'] * 100)
	happy = int(emozioni['happy'] * 100)
	#neutral = int(emozioni['neutral'] * 100)
	sad = int(emozioni['sad'] * 100)
	surprise = int(emozioni['surprise'] * 100)
	attention = int(emozioni['attention'] * 100)

	indice_gradimento = 50 - angry - disgust + happy - sad + surprise + attention

	if indice_gradimento > 55:
		return "si"
	else:
		return "no"







emozioni =  {'angry': 0.8, 'disgust': 0.3, 'happy': 0.1, 'neutral': 0.5, 'sad': 1, 'surprise': 0.2, 'attention': 0.3}

