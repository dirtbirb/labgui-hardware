import abc      # Abstract base class


class Device(abc.ABC):
    ''' Abstract base class for all hardware devices '''

    # TODO: ready/start/stop/close
    pass


class Sensor(Device):
    ''' Abstract base class for image capture devices, no focus stage '''

    def __init__(self, timeout=1):
        self.img = None
        self.sensor_x = None
        self.sensor_y = None
        self.temperature = 0
        self.timeout = timeout

    def ready(self):
        return True

    def start(self):
        return True

    def stop(self):
        return True

    def close(self):
        return True

    def get_img(self):
        pass

    # Sensor settings ---------------------------------------------------------
    def exposure(exp=None):
        pass

    def gain(gain=None):
        pass

    def fps(fps=None):
        pass

    def set_roi(roi={'x': None, 'y': None, 'h': None, 'w': None}):
        pass


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
