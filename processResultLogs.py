"""  
Created by FMartinez
Input: folder_path <string>
       percentage <float>  
Output: comma separated list of unique frame_numbers <file>
"""
import os
import sys
import time
import argparse
from pathlib import Path

# Use argparse to control the arguments of the script
parser = argparse.ArgumentParser()
parser.add_argument("folder_path", help="Folder where the log files to analyze are located.", type=str)
parser.add_argument("percentage", help="Percentage to filter frame numbers.", type=float)
args = parser.parse_args()

frameList = dict()
numberOfFiles = int()
resultFile = 'frame_numbers_percentage_'+str(int(time.time()))+'.log'

"""
Check that the percentage is between 0 and 100.
The tests for this should include different floats, values <0 and >100, letters, etc
"""
if (float(args.percentage) < 0 or float(args.percentage) > 100):
    sys.exit("Error: The percentage is not correct. It must be between 0 and 100.")


def processFrame( frameNumber ):
    """
    We define a function to process each individual frame value and increase the number
    of times it has already appeared in a log file.
    """
    if frameNumber in frameList:
        frameList[frameNumber] = frameList[frameNumber] + 1
    else:
        frameList[frameNumber] = 1
    return


def framePercentage( frame, percentage ):
    """
    Compare frame % with percentage parameter passed to script.
    """
    if frame-percentage < 0:
        return 0
    else:
        return 1


def parseFrameList( ):
    """
    Parse FrameList and check which values are inside the porcentage passed as paramter to
    the script.
    """
    for frame in frameList:
        if framePercentage(float(frameList[frame]*100/numberOfFiles),float(args.percentage)):
            writeResult(frame)
    print("Process Completed!")
    print("Number of log files analized: " + str(numberOfFiles))
    print('Results can be found in the file ' + resultFile + '\n')


def writeResult( frame ):
    """
    Write the results to the file defined at the beginning of the script.
    """
    with open(resultFile, "a") as myfile:
        myfile.write(frame+",")


"""
Get all the log files in the folder passed as parameter to the script.
Then we read all the files and store the frame_numbers in a dictionary
"""
for file in os.scandir(args.folder_path):
    if file.name.startswith('result_'):
        numberOfFiles += 1
        p = Path(args.folder_path + "/" + file.name)
        with p.open() as f:
            data_content = f.readlines()
        for i in range(len(data_content)):
            data_content[i] = data_content[i].split(",")[0]
            processFrame(data_content[i])


"""
Call the function to check if each frame_number is inside the percentage passed.
"""
parseFrameList()
