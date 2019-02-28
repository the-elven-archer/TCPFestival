import socket
import time


class TCPFestival():
    def __init__(self, host, port=1314):
        """Uses Festival TTS engine via TCP
        host -- Server hostname
        port -- Server port (default 1314)
        """
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """Connect to server
        """
        self.socket.connect((self.host, self.port))

    def disconnect(self):
        """Disconnect from server
        """
        self.socket.close()

    def _recvall(self):
        """Receives data from socket
        It must be executed after a "send" command
        """
        output = list()
        response = dict()
        output_type = str()
        with self.socket.makefile() as sfile:
            while True:
                line = sfile.readline()
                if "LP" in line:
                    output_type = "lisp"
                if "OK" in line:
                    exit = "ok"
                    break
                if "ER" in line:
                    exit = "error"
                    break
                if line.startswith("("):
                    output.append(line)
        response = {'type': output_type,
                    'output': output,
                    'exit': exit}
        return response

    def _sendcommand(self, command):
        """Send command to server
        """
        data = command.encode()
        self.socket.send(data)
        reply = self._recvall()
        return reply

    def sayText(self, text):
        """Say text using the engine
        text -- Text string
        """
        output = self._sendcommand("""(SayText "{}")""".format(text))
        return(output)

    def listVoices(self):
        """List the server available voices
        """
        output = self._sendcommand("""(voice.list)""")
        voices = list()
        for voice in " ".join(output['output']).replace("(", '').replace(")", '').split():
            voices.append(voice)
        return(voices)

    def changeVoice(self, voice):
        """Change current voice
        voice -- Festival voice name
        """
        output = self._sendcommand("""(voice_{})""".format(voice))
        return(output)

