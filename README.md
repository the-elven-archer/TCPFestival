# TCPFestival

The Festival TTS TCP Client

## Installation

```
$ pip3 install git+https://github.com/the-elven-archer/TCPFestival.git
```

## Usage: 

- Run `festival` in *server mode*:  
```
$ festival --server
server    Thu Feb 28 18:00:00 2019 : Festival server started on port 1314
```

- Import and use!
```python
from TCPFestival.tcpfestival import TCPFestival

tf = TCPFestival(host="localhost", port=1314)

tf.connect()

tf.sayText("HI! How are you? This is fun!")
{'type': 'lisp', 'output': [], 'exit': 'ok'}
```
You would hear the TTS synthesis from your computer.

You can list server voices:
```
tf.listVoices()
['kal_diphone', 'rab_diphone']
```

And change it:
```
tf.changeVoice("rab_diphone")
{'type': 'lisp', 'output': [], 'exit': 'ok'}
```
