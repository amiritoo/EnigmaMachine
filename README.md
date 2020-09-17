# EnigmaMachine

An **Enigma machine** is a famous encryption machine used by the Germans during WWII to transmit coded messages. An Enigma machine allows for billions and billions of ways to encode a message, making it incredibly difficult for other nations to crack German codes during the war — for a time the code seemed unbreakable. Alan Turing and other researchers exploited a few weaknesses in the implementation of the Enigma code and gained access to German codebooks, and this allowed them to design a machine called a Bombe machine, which helped to crack the most challenging versions of Enigma. Some historians believe that the cracking of Enigma was the single most important victory by the Allied powers during WWII. Using information that they decoded from the Germans, the Allies were able to prevent many attacks. However, to avoid Nazi suspicion that they had insight to German communications, the Allies had to allow some attacks to be carried out despite the fact that they had the knowledge to stop them. 


![](https://github.com/amiritoo/EnigmaMachine/blob/master/image/iVvdZithen-800px-enigma-plugboard.jpg)

**Enigma Encryption**

As mentioned in above sections, Enigma uses a form of substitution ciphers.

Each of the three rotors will display a number or letter (the rotors in the image above have letters), and when the rotors turn, a new set of three numbers/letters appears. With the initial set of three numbers/letters (meaning the numbers/letters on the sender’s machine when they began to type the message), a message recipient can decode the message by setting their (identical) Enigma machine to the initial settings of the sender’s Enigma machine. Each rotor has 262626 numbers/letters on it. An Enigma machine takes three rotors at a time, and the Germans could interchange rotors, choosing from a set of five, resulting in thousands of possible configurations. For example, one configuration of rotors could be: rotor #5 in slot one, rotor #2 in slot two, and rotor #1 in slot three.

**How many configurations are possible with an Enigma machine with these specifications?**

In the first slot, there are 555 rotors to pick from, in the second there are 444 rotors to pick from, and in the third slot there are 333 rotors to pick from. So there are 5×4×3=605 \times 4 \times 3 = 605×4×3=60 ways to configure the five rotors.

There are 262626 starting positions for each rotor, so there are 26×26×26=17,57626 \times 26 \times 26 = 17,576 26×26×26=17,576


first run the config_enigma.py for enimga configuration setting then run the main progmram enigma.py


hope u enjoy IT ;)
