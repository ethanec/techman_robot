# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from tm_msgs/RobotStateMsgRT.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class RobotStateMsgRT(genpy.Message):
  _md5sum = "b44d2ec991068109b7dfd7a73666f138"
  _type = "tm_msgs/RobotStateMsgRT"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """# Data structure for the realtime communications interface
# used by the Techman Robot controller
# 
# This data structure is send at 100 Hz on TCP port 6188

Header header
float64 time
float64 controller_time
float64[] q_command
float64[] qd_command
float64[] qt_command
float64[] q_actual
float64[] qd_actual
float64[] qt_actual
float64[] tool0_pos_command
float64[] tool0_pos_actual
float64[] tool_pos_command
float64[] tool_pos_actual
float64[] tcp_speed
float64[] tcp_force
int32[] kine_config
float64 common_speed_ratio
int32 robot_mode
int32 safety_mode
int32 teach_mode
int32 control_mode
int32 error_code_0
int32 error_code_1

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id
"""
  __slots__ = ['header','time','controller_time','q_command','qd_command','qt_command','q_actual','qd_actual','qt_actual','tool0_pos_command','tool0_pos_actual','tool_pos_command','tool_pos_actual','tcp_speed','tcp_force','kine_config','common_speed_ratio','robot_mode','safety_mode','teach_mode','control_mode','error_code_0','error_code_1']
  _slot_types = ['std_msgs/Header','float64','float64','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','float64[]','int32[]','float64','int32','int32','int32','int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,time,controller_time,q_command,qd_command,qt_command,q_actual,qd_actual,qt_actual,tool0_pos_command,tool0_pos_actual,tool_pos_command,tool_pos_actual,tcp_speed,tcp_force,kine_config,common_speed_ratio,robot_mode,safety_mode,teach_mode,control_mode,error_code_0,error_code_1

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RobotStateMsgRT, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.time is None:
        self.time = 0.
      if self.controller_time is None:
        self.controller_time = 0.
      if self.q_command is None:
        self.q_command = []
      if self.qd_command is None:
        self.qd_command = []
      if self.qt_command is None:
        self.qt_command = []
      if self.q_actual is None:
        self.q_actual = []
      if self.qd_actual is None:
        self.qd_actual = []
      if self.qt_actual is None:
        self.qt_actual = []
      if self.tool0_pos_command is None:
        self.tool0_pos_command = []
      if self.tool0_pos_actual is None:
        self.tool0_pos_actual = []
      if self.tool_pos_command is None:
        self.tool_pos_command = []
      if self.tool_pos_actual is None:
        self.tool_pos_actual = []
      if self.tcp_speed is None:
        self.tcp_speed = []
      if self.tcp_force is None:
        self.tcp_force = []
      if self.kine_config is None:
        self.kine_config = []
      if self.common_speed_ratio is None:
        self.common_speed_ratio = 0.
      if self.robot_mode is None:
        self.robot_mode = 0
      if self.safety_mode is None:
        self.safety_mode = 0
      if self.teach_mode is None:
        self.teach_mode = 0
      if self.control_mode is None:
        self.control_mode = 0
      if self.error_code_0 is None:
        self.error_code_0 = 0
      if self.error_code_1 is None:
        self.error_code_1 = 0
    else:
      self.header = std_msgs.msg.Header()
      self.time = 0.
      self.controller_time = 0.
      self.q_command = []
      self.qd_command = []
      self.qt_command = []
      self.q_actual = []
      self.qd_actual = []
      self.qt_actual = []
      self.tool0_pos_command = []
      self.tool0_pos_actual = []
      self.tool_pos_command = []
      self.tool_pos_actual = []
      self.tcp_speed = []
      self.tcp_force = []
      self.kine_config = []
      self.common_speed_ratio = 0.
      self.robot_mode = 0
      self.safety_mode = 0
      self.teach_mode = 0
      self.control_mode = 0
      self.error_code_0 = 0
      self.error_code_1 = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d().pack(_x.time, _x.controller_time))
      length = len(self.q_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.q_command))
      length = len(self.qd_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qd_command))
      length = len(self.qt_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qt_command))
      length = len(self.q_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.q_actual))
      length = len(self.qd_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qd_actual))
      length = len(self.qt_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.qt_actual))
      length = len(self.tool0_pos_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tool0_pos_command))
      length = len(self.tool0_pos_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tool0_pos_actual))
      length = len(self.tool_pos_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tool_pos_command))
      length = len(self.tool_pos_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tool_pos_actual))
      length = len(self.tcp_speed)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tcp_speed))
      length = len(self.tcp_force)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.tcp_force))
      length = len(self.kine_config)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.Struct(pattern).pack(*self.kine_config))
      _x = self
      buff.write(_get_struct_d6i().pack(_x.common_speed_ratio, _x.robot_mode, _x.safety_mode, _x.teach_mode, _x.control_mode, _x.error_code_0, _x.error_code_1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.time, _x.controller_time,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_command = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_command = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qt_command = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qt_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool0_pos_command = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool0_pos_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_pos_command = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_pos_actual = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_speed = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_force = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.kine_config = s.unpack(str[start:end])
      _x = self
      start = end
      end += 32
      (_x.common_speed_ratio, _x.robot_mode, _x.safety_mode, _x.teach_mode, _x.control_mode, _x.error_code_0, _x.error_code_1,) = _get_struct_d6i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2d().pack(_x.time, _x.controller_time))
      length = len(self.q_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.q_command.tostring())
      length = len(self.qd_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qd_command.tostring())
      length = len(self.qt_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qt_command.tostring())
      length = len(self.q_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.q_actual.tostring())
      length = len(self.qd_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qd_actual.tostring())
      length = len(self.qt_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.qt_actual.tostring())
      length = len(self.tool0_pos_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tool0_pos_command.tostring())
      length = len(self.tool0_pos_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tool0_pos_actual.tostring())
      length = len(self.tool_pos_command)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tool_pos_command.tostring())
      length = len(self.tool_pos_actual)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tool_pos_actual.tostring())
      length = len(self.tcp_speed)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tcp_speed.tostring())
      length = len(self.tcp_force)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.tcp_force.tostring())
      length = len(self.kine_config)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.kine_config.tostring())
      _x = self
      buff.write(_get_struct_d6i().pack(_x.common_speed_ratio, _x.robot_mode, _x.safety_mode, _x.teach_mode, _x.control_mode, _x.error_code_0, _x.error_code_1))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 16
      (_x.time, _x.controller_time,) = _get_struct_2d().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_command = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_command = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qt_command = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.q_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qd_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.qt_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool0_pos_command = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool0_pos_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_pos_command = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tool_pos_actual = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_speed = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.tcp_force = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.kine_config = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      _x = self
      start = end
      end += 32
      (_x.common_speed_ratio, _x.robot_mode, _x.safety_mode, _x.teach_mode, _x.control_mode, _x.error_code_0, _x.error_code_1,) = _get_struct_d6i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2d = None
def _get_struct_2d():
    global _struct_2d
    if _struct_2d is None:
        _struct_2d = struct.Struct("<2d")
    return _struct_2d
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_d6i = None
def _get_struct_d6i():
    global _struct_d6i
    if _struct_d6i is None:
        _struct_d6i = struct.Struct("<d6i")
    return _struct_d6i
