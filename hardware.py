import abc      # Abstract base class


class Device(abc.ABC):
    ''' Abstract base class for all hardware devices '''

    def __init__(self, timeout=1):
        self.available = False
        self.running = False
        self.timeout = timeout

    def start(self):
        return True

    def close(self):
        return True


class Sensor(Device):
    ''' Abstract base class for image capture devices, no focus stage '''

    def __init__(self, img_queue, timeout=1):
        super().__init__(timeout)
        self.img_queue = img_queue

    def exposure(self, exp=None):
        return exp

    def gain(self, gain=None):
        return gain

    def fps(self, fps=None):
        return fps

    def roi(self, roi=(None, None, None, None)):
        return (0., 0., 1., 1.)


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

    def move_to(self, dest):
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
