# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

from IPython.display import HTML

def system():
    return HTML('<img src="images/ibm_system.jpg" width="1000 px" align="center">')

def simple_2qubits():
    return HTML('<img src="images/simple-2-qubits.png" width="282 px" align="center">')

def super_def():
    return HTML('''<br />

<p style="width: 500px;">
  <b>Superposition</b> is a fundamental principle of quantum mechanics stating that a physical system – such as a photon or electron – simultaneously exists partly in all theoretically possible states; but when measured or observed gives a result corresponding to only one of the possible states.
</p>
<br />
https://phys.org/news/2014-10-superposition-revisited-resolution-double-slit-paradox.amp

<br /><br /><br />

<p style="width: 500px;">
  <b>More simply put:</b> A quantum entity exists in a superposition when it is in 2 or more states (or positions) at once. When observed, it becomes one of the states, and acts as if it was in that state all along.
</p>
<br /><br /><br /><br /><br /><br />''')

def feynman_quote():
    return HTML('''
<blockquote>
<p>
The double-slit experiment has in it the heart of quantum mechanics. In reality, it contains the only mystery.
</p>
<footer>Richard Feynman</footer>
</blockquote>
    ''')

def double_slit1():
    return HTML('''<img src="images/Double-slit.png" width="560 px"><br />By <a href="//commons.wikimedia.org/wiki/File:Double-slit.PNG" title="File:Double-slit.PNG">Original: </a><a href="//commons.wikimedia.org/wiki/User:NekoJaNekoJa~commonswiki" title="User:NekoJaNekoJa~commonswiki">NekoJaNekoJa</a>Vector:<a href="https://de.wikipedia.org/wiki/Benutzer:JoKalliauer" class="extiw" title="de:Benutzer:JoKalliauer">Johannes Kalliauer</a> - <a href="//commons.wikimedia.org/wiki/File:Double-slit.PNG" title="File:Double-slit.PNG">File:Double-slit.PNG</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=61496401">Link</a>''')

def double_slit2():
    return HTML('''<img src="images/Single_slit_and_double_slit2.jpg" width="560 px"><br />By <a href="//commons.wikimedia.org/w/index.php?title=User:Jordgette&amp;action=edit&amp;redlink=1" class="new" title="User:Jordgette (page does not exist)">Jordgette</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=9529698">Link</a>''')

def double_slit():
#    <img src="images/add-waves-3.png" width="807 px"> # actual image is 807 wide
    return HTML('''
    <img src="images/add-waves-3.png" width="400 px">
    <img src="images/Double-slit.png" width="400 px"><br />By <a href="//commons.wikimedia.org/wiki/File:Double-slit.PNG" title="File:Double-slit.PNG">Original: </a><a href="//commons.wikimedia.org/wiki/User:NekoJaNekoJa~commonswiki" title="User:NekoJaNekoJa~commonswiki">NekoJaNekoJa</a>Vector:<a href="https://de.wikipedia.org/wiki/Benutzer:JoKalliauer" class="extiw" title="de:Benutzer:JoKalliauer">Johannes Kalliauer</a> - <a href="//commons.wikimedia.org/wiki/File:Double-slit.PNG" title="File:Double-slit.PNG">File:Double-slit.PNG</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=61496401">Link</a>
    <img src="images/Single_slit_and_double_slit2.jpg" width="400 px"><br />By <a href="//commons.wikimedia.org/w/index.php?title=User:Jordgette&amp;action=edit&amp;redlink=1" class="new" title="User:Jordgette (page does not exist)">Jordgette</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=9529698">Link</a>
    ''')

def schrodinger_quote():
    return HTML('''
<blockquote>
<p>
I would not call [entanglement] <i>one</i> but rather <i>the</i> characteristic trait of quantum mechanics, 
the one that enforces its entire departure from classical lines of thought.
</p>
<footer>Erwin Schrödinger</footer>
</blockquote>
    ''')

def mermin_quote():
    return HTML('''
<blockquote>
<p>
The EPR experiment is as close to magic as any physical phenomenon I know of, and magic should be enjoyed.
</p>
<footer>N. David Mermin</footer>
</blockquote>
    ''')

def einstein_dice():
    return HTML('''
<blockquote>
<p>
I, at any rate, am convinced that [God] does not throw dice.
</p>
<footer>Albert Einstein</footer>
</blockquote>
    ''')

def bohr_response():
    return HTML('''
<blockquote>
<p>
Stop telling God what to do with his dice.
</p>
<footer>Niels Bohr</footer>
</blockquote>
    ''')

def epr_nyt():
    return HTML('''<img src="images/NYT_May_4,_1935.jpg" width="247 px">
    Article headline regarding the Einstein–Podolsky–Rosen paradox (EPR paradox) paper, in the May 4, 1935 issue of The New York Times.
    <br />
    ''')

def einstein_vs_bohr():
    # TODO: use style sheet
    return HTML('''
<table style="border: 1px solid black;">
<tr><th style="border: 1px solid black;text-align:left">Einstein camp</th><th style="border: 1px solid black;text-align:left">Bohr camp / Quantum theory</th></tr>
<tr><td style="border: 1px solid black;text-align:left">locality</td><td style="border: 1px solid black;text-align:left">entanglement E:"spooky action at a distance"</td></tr>
<tr><td style="border: 1px solid black;text-align:left">realism E:"The moon is there even if I am not looking at it."</td><td style="border: 1px solid black;text-align:left">reality doesn’t exist until it is measured</td></tr>
<tr><td style="border: 1px solid black;text-align:left">deterministic / hidden variables E:"God does not play dice"</td><td style="border: 1px solid black;text-align:left">superposition / random</td></tr>
<tr><td style="border: 1px solid black;text-align:left">makes sense</td><td style="border: 1px solid black;text-align:left">strange</td></tr>
</table>
    ''')

def Bell_CHSH_inequality():
    return HTML('''<img src="images/bell_chsh_slide.png" width="954 px"><br />''')

def bell_truth_table():
    # TODO: use style sheet
    return HTML('''
<table style="border: 1px solid black;">
<tr><th style="border: 1px solid black;text-align:left">local</th><th style="border: 1px solid black;text-align:left">hidden var</th><th style="border: 1px solid black;text-align:left"></th></tr>
<tr><td style="border: 1px solid black;text-align:left">yes</td><td style="border: 1px solid black;text-align:left">no</td><td style="border: 1px solid black;text-align:left"><del>Would not see correlation.</del></td></tr>
<tr><td style="border: 1px solid black;text-align:left">yes</td><td style="border: 1px solid black;text-align:left">yes</td><td style="border: 1px solid black;text-align:left"><del>Einstein/EPR - Bell experiment rules out.</del></th></td>
<tr><td style="border: 1px solid black;text-align:left">no</td><td style="border: 1px solid black;text-align:left">no</td><td style="border: 1px solid black;text-align:left">Entanglement. Most popular.</th></td>
<tr><td style="border: 1px solid black;text-align:left">no</td><td style="border: 1px solid black;text-align:left">yes</td><td style="border: 1px solid black;text-align:left">Also in the running. Pilot wave theory is an example.</td></tr>
</table>
    ''')

print('loaded')
