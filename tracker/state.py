import logging


class State:
    def __init__(self, PAUSE=False, LOOP=True, INCR=0):
        self.__PAUSE = PAUSE
        self.__LOOP = LOOP
        self.__INCR = INCR
        self.__PAUSE_callbacks = []
        self.__LOOP_callbacks = []
        self.__INCR_callbacks = []

    @property
    def PAUSE(self):
        return self.__PAUSE

    @PAUSE.setter
    def PAUSE(self, new_value):
        old_value = self.__PAUSE
        self.__PAUSE = new_value
        self.__notify_observers('PAUSE', old_value, new_value)

    @property
    def LOOP(self):
        return self.__LOOP

    @LOOP.setter
    def LOOP(self, new_value):
        old_value = self.__LOOP
        self.__LOOP = new_value
        self.__notify_observers('LOOP', old_value, new_value)

    @property
    def INCR(self):
        return self.__INCR

    @INCR.setter
    def INCR(self, new_value):
        old_value = self.__INCR
        self.__INCR = new_value
        self.__notify_observers('INCR', old_value, new_value)

    def register_callback(self, state_variable, callback):
        if state_variable == 'PAUSE':
            self.__PAUSE_callbacks.append(callback)
        elif state_variable == 'LOOP':
            self.__LOOP_callbacks.append(callback)
        elif state_variable == 'INCR':
            self.__INCR_callbacks.append(callback)

    def __notify_observers(self, state_variable, old_value, new_value):
        if state_variable == 'PAUSE':
            for callback in self.__PAUSE_callbacks:
                callback(old_value, new_value)
        elif state_variable == 'LOOP':
            for callback in self.__LOOP_callbacks:
                callback(old_value, new_value)
        elif state_variable == 'INCR':
            for callback in self.__INCR_callbacks:
                callback(old_value, new_value)


def dummy_callback(*args):
    for arg in args:
        print(arg)


if __name__ == '__main__':
    dum_state = State()
    dum_state.register_callback('PAUSE', dummy_callback)
    dum_state.register_callback('LOOP', dummy_callback)
    dum_state.register_callback('INCR', dummy_callback)
    dum_state.PAUSE = True
    dum_state.LOOP = True
    dum_state.INCR += 1
