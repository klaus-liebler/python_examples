import candle_driver

# lists all available candle devices
devices = candle_driver.list_devices()

if not len(devices):
  print('No candle devices found.')
  exit()

print('Found {} candle devices.'.format(len(devices)))

# use first availabel device
device = devices[0]

print('Device path: {}'.format(device.path()))
print('Device name: {}'.format(device.name()))
print('Device channels: {}'.format(device.channel_count()))

# open device (blocks other processes from using it)
device.open()

print('Device timestamp: %d' % device.timestamp()) # in usec

# open first channel
ch = device.channel(0)

ch.set_bitrate(1000000)
# or
# ch.set_timings(prop_seg=1, phase_seg1=12, phase_seg2=2, sjw=1, brp=3)

# start receiving data
ch.start()

# normal frame
ch.write(10, b'abcdefgh')
# extended frame
ch.write(10235 | candle_driver.CANDLE_ID_EXTENDED, b'abcdefgh')

# wait 1000ms for data
try:
  frame_type, can_id, can_data, extended, ts = ch.read(1000)
  print('Received {} from ID {} at {}'.format(can_data, can_id, ts))
except TimeoutError:
  print('CAN read timeout')

# close everything
ch.stop()
device.close()