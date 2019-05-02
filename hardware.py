import abc      # Abstract base class


class Device(abc.ABC):
    ''' Abstract base class for all hardware devices '''

    def __init__(self, timeout=1):
        self.running = False
        self.timeout = timeout

    def start(self):
        return True

    def close(self):
        return True


class Sensor(Device):
    ''' Abstract base class for image capture devices, no focus stage '''

    def exposure(exp=None):
        return exp

    def gain(gain=None):
        return gain

    def fps(fps=None):
        return fps

    def roi(roi=(None, None, None, None)):
        return roi


class Stage(Device):
    ''' Abstract base class for movement stages '''

    def __init__(self, timeout=1):
        self.homed = False
        self.pos = None
        self.timeout = timeout

        self.cal_data = None
        self.pos_data = None

    def is_moving(self):
        return False

    def get_position(self):
        return self.pos

    def move_by(dist):
        pass

    def move_to(dest):
        pass

    def home(self):
        pass

    def wait(self):
        pass


class LinearStage(Stage):
    ''' Abstract class for linear stages '''

    def __init__(self, timeout=None):
        super().__init__(timeout)

    def get_limits(self):
        return {"cw_limit": False, "ccw_limit": False}


class XYStage(Stage):
    ''' Abstract class for XY stages '''

    def __init__(self, timeout=None):
        super().__init__(timeout)
        self.pos = (None, None)
