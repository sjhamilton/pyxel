class Sound:
    def __init__(self, speed, data):
        self.speed = max(speed, 1)
        self.note = self._parse_note(data[0])
        self.length = len(self.note)
        self.inst = self._parse_param(data[1])
        self.volume = self._parse_param(data[2])
        self.effect = self._parse_param(data[3])

    def _parse_note(self, data):
        note = []
        data = data.replace(' ', '').upper()
        last_n = None

        while data:
            c = data[0]
            data = data[1:]

            if c >= 'A' and c <= 'G':
                n = [9, 11, 0, 2, 4, 5, 7][ord(c) - ord('A')]

                c = data[0]
                data = data[1:]

                if c == '#':
                    n += 1

                    c = data[0]
                    data = data[1:]

                if c >= '0' and c <= '9':
                    n += int(c) * 12
                else:
                    raise ValueError('invalid sound note')

            elif c == '.':
                n = last_n
            elif c == 'R':
                n = None
            else:
                raise ValueError('invalid sound note')

            note.append(n)
            last_n = n

        return note

    def _parse_param(self, data):
        param = []
        data = data.replace(' ', '').upper()

        while data:
            c = data[0]
            data = data[1:]

            if c >= '0' and c <= '7':
                param.append(int(c))
            else:
                raise ValueError('invalid sound data')

        diff = len(param) - self.length

        if diff < 0:
            param += [param[-1]] * -diff
        elif diff > 0:
            param = param[:self._length]

        return param
