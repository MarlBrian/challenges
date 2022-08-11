from DataCapture import DataCapture

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    stats.less(4)
    stats.between(3,6)
    stats.greater(4)
