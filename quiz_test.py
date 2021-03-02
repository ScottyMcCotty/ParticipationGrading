
from canvasapi import Canvas
import urllib.request
import pandas as pd
import pprint
from parseStudent import parse
from StudentClass import Student
from GroupClass import Group
from InteractionClass import Interaction
from func_utils import *

# big ideas:

# User inputs the url
# User inputs their api_key
# User inputs (or chooses) the user
# User inputs (or chooses) the course id
# User inputs (or chooses) the quiz id
# All user submissions get downloaded
# more stuff happens


# potentially useful API functions:
# course .get_quizzes() returns a list of quizzes
# course .get_recent_students() returns a list of students in order
                            # of how recently they've logged on
# course .get_user(userID) returns the User
# course .get_users() returns all users!
# quiz .get_submissions() returns all submissions
# quiz .get_statistics() returns all statistics (rebeca said this was good?)
# quizSubmission .get_submission_questions() returns quizSubmissionQuestion's
# quizSubmission .update_score_and_comments() somehow send the "fudge points"??

    
##############################
######## Main Function #######
##############################

if __name__ == "__main__":
    
    # get user input for the url
    url = getAPIURL()
    print("Got url: '",url,"'",sep='')

    # get user input for the api key
    key = getAPIKEY()
    print("Got key: '",key,"'",sep='')

    # now we have enough information to make our canvas object
    canvas = getCanvas(url, key)
    print("Got canvas: '",canvas,"'",sep='')

    # OHH OKAY IT LOOKS LIKE THIS ONE MIGHT NOT EVEN BE NEEDED! WHOOPS
    # get user input for the canvas's user
    user = getUser(canvas)
    print("Got user: '",user,"'",sep='')
    
    # get user input for the course
    course = getCourse(canvas)
    print("Got course: '",course,"'",sep='')
    
    # get the groups of a particular course
    groups = getGroups(course)

    # convert each group to a Group object
    # then put them into a master group_list
    group_list = []
    for group in groups:
        g = Group(group)
        group_list.append(g)

    # create a dictionary mapping each group_id to their students
    # remember that each student has an attribute identifying their group as well
    group_dict = {}
    for g in group_list:
        group_dict[g.getID()] = g.getStudents()
        
        # print(g.getName())
        # print(g.getID())
        # print(g.getStudents())

    # print(group_dict)
    # exit()
    
    # get the user input for the quiz
    quiz = getQuiz(course)
    print("Got quiz: '",quiz,"'",sep='')

    # print all submissions for a particular quiz
    submissions = quiz.get_submissions()
    all_interactions = []
    print("Got submissions: ")
    for submission in submissions:
        print(submission)
        # all_interactions = recordSubmission(submission, all_interactions)

    # what the recordSubmission(submission, all_interactions) call should do:
        # look at all user submissions
        # parse question answers
        # for each question:
            # ignore if answer to the first drop-down is 'None'
            # otherwise, create an Interaction object which notes:
                # activity type
                # duration (set to 0 if no duration was selected)
                # list of students involved, including the user who submitted (set to empty list if no selection)
                # Interaction ID, composed of user_id + submission_id + i (i=1,2,3,4)
            # append each valid Interaction to all_interactions
        # return all_interactions


    # Now look at submissions by Group

    # gradeSubmission(submission, all_interactions)

    # what the gradeSubmission(submission) call should do:
        # get the user the submission belongs to
        # parse question answers
        # for each question:
            # ignore if answer to the first drop-down is 'None'
            # otherwise, create an Interaction object the same way as before
            # check against existing list of Interactions for all four attributes
                # activity type (give this a lower weight if everything else matches?)
                # duration
                    # allow for +/- 5min buffer in duration
                # list of students involved, including the user who submitted (set to empty list if no selection)
                    # check to make sure all students selected are in the specified Group
                # Interaction ID, composed of user_id + submission_id + i (i=1,2,3,4)
                    # Do not count valid Interaction if the ID is the same
               
            # if Interaction exists, tally up time

        # calculate grade from time / 20
        # return grade

    # Interaction object
    # Attributes:
        # students involved
        # duration
        # activity

    # get user input for the assignment
    #assignment = getAssignment(course)
    #print("Got assignment: '",assignment,"'",sep='')

    #getQuizSubmissions(quiz)
    #getSubmissions(quiz)
    
    #quiz = canvasClass.get_quiz(QUIZ_ID)
    studentReport = quiz.create_report("student_analysis")
    # print(studentReport.__dict__)
    url = studentReport.file["url"]
    studentData = pd.read_csv(url)

    # Get the right quiz
    studentReport = quiz.create_report("student_analysis")
    reportProgress = None

    # URL of canvas progress object from studentReport
    reportProgressURL = studentReport.progress_url

    # parse so only the process id remains
    prefix = 'https://canvas.ucdavis.edu/api/v1/progress/'
    if reportProgressURL.startswith(prefix):
        reportProgressID = reportProgressURL[len(prefix):]
    else: 
        reportProgressID = reportProgressURL

    # wait for student report to finish generating while the process has not completed or failed 
    while reportProgress != 'completed' and reportProgress != 'failed':
        reportProgressObj = canvas.get_progress(reportProgressID)
        reportProgress = reportProgressObj.workflow_state

    studentReportN = quiz.create_report("student_analysis")
    url = studentReportN.file["url"]
    studentData = pd.read_csv(url)

    parse(studentData, course.id)