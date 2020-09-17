# EnigmaMachine

An **Enigma machine** is a famous encryption machine used by the Germans during WWII to transmit coded messages. An Enigma machine allows for billions and billions of ways to encode a message, making it incredibly difficult for other nations to crack German codes during the war — for a time the code seemed unbreakable. Alan Turing and other researchers exploited a few weaknesses in the implementation of the Enigma code and gained access to German codebooks, and this allowed them to design a machine called a Bombe machine, which helped to crack the most challenging versions of Enigma. Some historians believe that the cracking of Enigma was the single most important victory by the Allied powers during WWII. Using information that they decoded from the Germans, the Allies were able to prevent many attacks. However, to avoid Nazi suspicion that they had insight to German communications, the Allies had to allow some attacks to be carried out despite the fact that they had the knowledge to stop them. 


![](https://github.com/amiritoo/EnigmaMachine/blob/master/image/iVvdZithen-800px-enigma-plugboard.jpg)

**Encryption**

Enigma machines use a form of substitution encryption.

Substitution encryption is a straightforward way of encoding messages, but these codes are fairly easy to break. A simple example of a substitution encryption scheme is a Caesar cipher. A Caesar cipher shifts each letter of the alphabet some number of places. A Caesar cipher with a shift of 111 would encode an A as a B, an M as an N, and a Z as an A, and so on. 



**How an Enigma Machine Works**

An Enigma machine is made up of several parts including a keyboard, a lamp board, rotors, and internal electronic circuitry. Some machines, such as the ones used by the military, have additional features such as a plugboard.


Encoded messages would be a particular scramble of letters on a given day that would would translate to a comprehendible sentence when unscrambled.

When a key on the keyboard is pressed, one or more rotors move to form a new rotor configuration which will encode one letter as another. Current flows through the machine and lights up one display lamp on the lamp board, which shows the output letter. So if the "K" key is pressed, and the Enigma machine encodes that letter as a "P," the "P" would light up on the lamp board.

Each month, Enigma operators received codebooks which specified which settings the machine would use each day. Every morning the code would change.

For example, one one day, the codebook may list the settings described in the day-key below:

1.1.1. Plugboard settings: A/L – P/R – T/D – B/W – K/F – O/Y

A plugboard is similar to an old-fashioned telephone switch board that has ten wires, each wire having two ends that can be plugged into a slot. Each plug wire can connect two letters to be a pair (by plugging one end of the wire to one letter’s slot and the other end to another letter). The two letters in a pair will swap over, so if “A” is connected to “Z,” “A” becomes “Z” and “Z” becomes “A.” This provides an extra level of scrambling for the military.

To implement this day-key first you would have to swap the letters A and L by connecting them on the plugboard, swap P and R by connecting them on the plugboard, and then the same with the other letter pairs listed above. Essentially, a one end of a cable would be plugged into the "A" slot and the other end would be plugged into the L slot. Before any further scrambling happens by the rotors, this adds a first layer of scrambling where the letters connected by the cable are encoded as each other. For example, if I were to encode the message APPLE after connecting only the "A" to the "L", this would be encoded as LPPAE.

The plugboard is positioned at the front of an Enigma machine, below the keys. The plugboard is positioned at the front of an Enigma machine, below the keys.

2.2.2. Rotor (or scrambler) arrangement: 2 — 3 —1

The Enigma machines came with several different rotors, each rotor providing a different encoding scheme. In order to encode a message, the Enigma machines took three rotors at a time, one in each of three slots. Each different combination of rotors would produce a different encoding scheme. Note: most military Enigma machines had three rotor slots though some had more.

To accomplish the configuration above, place rotor #2 in the 1st slot of the enigma, rotor #3 in the 2nd slot, and rotor #1 in the 3rd slot.

3.3.3. Rotor orientations: D – K –P

On each rotor, there is an alphabet along the rim, so the operator can set in a particular orientation. For this example, the operator would turn the rotor in slot 1 so that D is displayed, rotate the second slot so that K is displayed, and rotate the third slot so that P is displayed. 

**Enigma Encryption**

As mentioned in above sections, Enigma uses a form of substitution ciphers.

Each of the three rotors will display a number or letter (the rotors in the image above have letters), and when the rotors turn, a new set of three numbers/letters appears. With the initial set of three numbers/letters (meaning the numbers/letters on the sender’s machine when they began to type the message), a message recipient can decode the message by setting their (identical) Enigma machine to the initial settings of the sender’s Enigma machine. Each rotor has 262626 numbers/letters on it. An Enigma machine takes three rotors at a time, and the Germans could interchange rotors, choosing from a set of five, resulting in thousands of possible configurations. For example, one configuration of rotors could be: rotor #5 in slot one, rotor #2 in slot two, and rotor #1 in slot three.

**How many configurations are possible with an Enigma machine with these specifications?**

In the first slot, there are 555 rotors to pick from, in the second there are 444 rotors to pick from, and in the third slot there are 333 rotors to pick from. So there are 5×4×3=605 \times 4 \times 3 = 605×4×3=60 ways to configure the five rotors.

There are 262626 starting positions for each rotor, so there are 26×26×26=17,57626 \times 26 \times 26 = 17,576 26×26×26=17,576


first run the config_enigma.py for enimga configuration setting then run the main progmram enigma.py


hope u enjoy IT ;)
