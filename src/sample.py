'''
Created on Oct 4, 2011

This sample code provides a sample on how to output TAP in Jython using 
tap4j - http://www.tap4j.org.

The required libraries are in ${project.basedir}/lib. For a complete list of 
the dependencies of tap4j, please refer to the project's pom.xml in github.

@author: Bruno P. Kinoshita - http://www.kinoshita.eti.br
@since 1.0
'''
from org.tap4j.model import TestSet, TestResult, Plan
from org.tap4j.producer import TapProducerFactory
from org.tap4j.util import StatusValues
import java.io.File
import sys

# A TAP Test Set
testSet  = TestSet()
# Here we say that our plan contains 2 tests
testSet.setPlan(Plan(2))

# Create the first Test Result
testResult1 = TestResult()
testResult1.setTestNumber(1)
testResult1.setStatus(StatusValues.OK)
testResult1.setDescription("- no error")

# Add it to Test Set
testSet.addTestResult(testResult1);

# Create the second Test Result
testResult2 = TestResult()
testResult2.setTestNumber(2)
testResult2.setStatus(StatusValues.NOT_OK)
testResult2.setDescription("- failed for some reason")

# Add it to Test Set
testSet.addTestResult(testResult2)

tapFile = java.io.File("../output.tap")

# If the file already exists, then we delete it
if tapFile.exists() :
    tapFile.delete()

# create a new file
if tapFile.createNewFile() == False:
    print "Failed to create new file"
    sys.exit(-1)

# create the TAP Producer, there is another TAP Producer that supports YAMLish 
# diagnostics
producer = TapProducerFactory.makeTap13Producer()

# Dump the Test Set into the output file
producer.dump(testSet, tapFile);

print "OK!"