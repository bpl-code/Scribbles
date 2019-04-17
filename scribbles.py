#Scribbles.py
#A smart to do list with note taking ablility

#dependiences
from datetime import datetime


class toDoList():
    def __init__(self):
        self.toDoListFull = []
        self.toDoHigh = []
        self.toDoLow = []
        self.completedTasks = []
        

    #get functions

    def getHighPriorityList(self):
        return self.toDoHigh

    def getLowPriorityList(self):
        return self.toDoLow

    #Core functions

    def addTask(self, task):
        if task.getPriority() == "high":
            self.toDoHigh.append(task)
        elif task.getPriority() == "low":
            self.toDoLow.append(task)

    def completeTask(self, task):
        task.complete()

    def undoCompleteTask(self, task):
        task.incompleteTask()


    



class task():
    def __init__(self, task):
        self.task = task
        self.dateAndTime = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.priority = ''
        self.deadline = ""
        self.notes = []
        self.taskComplete = False

    #Get functions

    def getTask(self):
        return self.task

    def getDate(self):
        date = self.dateAndTime.split()
        return date[0]

    def getTime(self):
        time = self.dateAndTime.split()
        return time[1]

    def getDateAndTime(self):
        return self.dateAndTime

    def getPriority(self):
        return self.priority

    def getDeadline(self):
        return self.deadline

    def getNotes(self):
        return self.notes

    def getNumOfNotes(self):
        return len(self.notes)

    def setDeadline(self, deadline):
        self.deadline = deadline

    def setPriority(self, priority):
        self.priority = priority

    #Core functions

    def complete(self):
        self.taskComplete = True
    
    def incomplete(self):
        self.taskComplete = False

    
    #Note based functions

    def addNote(self, note):
        note.linkTask(self.task)
        self.notes.append(note)

    def removeNote(self, note):
        self.notes.remove(note)
        note.removeLinkedTask()

    def completeNote(self, note):
        note.completed()

    def incompleteNote(self, note):
        note.incomplete()

    def getProgress(self):
        tasks = []

        if self.notes:

            for note in self.notes:
                if note.isSubtask:
                    tasks.append(note)
                else:
                    pass

            totalsTasks = len(tasks)
            completedTasks = 0

            if len(tasks) > 0:
            
                for task in tasks: 
                    if task.noteCompleted:
                        completedTasks += 1 
                return "{} out of {} tasks have been completed.".format(completedTasks, totalsTasks)

            else:
                return "No sub-tasks have been assigned to this task."

        else:

            return "You have no notes or sub-tasks assigned to this task "


    




class note():
    def __init__(self, note):
        self.textNote = ""
        self.phoneNumber = ""
        self.email = ""
        self.website = ""
        self.contact = ""
        self.cost = ""
        self.dateAndTime = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
        self.deadline = ""
        self.linkedTask = ""
        self.assignmentCode = ""
        self.noteType = ""
        self.noteCompleted = False
        self.isSubtask = False

        #Assigns the note to the correct varible
        self.assignNote(note)


    #Get functions

    def getText(self):
        return self.textNote

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    def getWebsite(self):
        return self.website

    def getContact(self):
        return self.contact

    def getCost(self):
        return self.cost

    def getDate(self):
        date = self.dateAndTime.split()
        return date[0]

    def getTime(self):
        time = self.dateAndTime.split()
        return time[1]

    def getDateAndTime(self):
        return self.dateAndTime

    def getDeadline(self):
        return self.deadline

    def getLinkedTask(self):
        return self.linkedTask

    def getAssignmentCode(self):
        return self.assignmentCode

    def getNoteType(self):
        return self.noteType

    
    
    #Data Assignment Functions

    def assignNote(self, note):
        #Assigns the note to the correct type varible based on it's assign code
        try:
            assignmentCodes = {"@" : "self.email", "#" : "self.phoneNumber"}
            assignedCode = assignmentCodes[note[0]] 
            noteAssignment = assignedCode + " = '" + note[1:] + "'"
            exec(noteAssignment)
        except KeyError:
            self.textNote = note
            assignedCode = "self.textNote"
        
        self.assignmentCode = assignedCode
        self.noteType = assignedCode[5:]

    def addTextNote(self, note):
        self.textNote = note
        
    def requestAdditionalInfo(self):
        #Asks the user for additional information based on the type of note
        noteType = self.getAssignmentCode()
        additionalInfoRequests = {"self.email" : "Would you like to add a contact name and website for this email?", "self.phoneNumber" : "Would you like to add a contact name for this number?", "self.textNote" : "Note saved!", "=" : "self.cost"}
        return additionalInfoRequests[noteType]

    def addAdditionalInfo(self, userInput):
        #Adds additonal info to the note's varibles based on the note type. 
        noteAssigmentCode = self.getAssignmentCode()
        UIcounter = -1
        optionalInfo = {"self.email" : ("self.contact", "self.website"), "self.phoneNumber" : "self.contact", "self.cost" : "self.text"}

        if isinstance(userInput, str):
            exec(optionalInfo[noteAssigmentCode] + " = '" + userInput + "'")
        else:
            for assignments in optionalInfo[noteAssigmentCode]:
                UIcounter += 1
                exec(assignments + " = '" + userInput[UIcounter] + "'")
    
    def scanNoteForInfo(self):
        #Scans a plain text note for assignable info
        splitText = self.textNote.split()

        for word in splitText:
            if self.checkForEmail(word):
                self.email = word
            elif self.checkForPhoneNumber(word):
                self.phoneNumber = word
            elif self.checkForWebsite(word):
                self.website = word
            elif self.checkForCost(word):
                self.cost = word
    

    def checkForEmail(self, userString):
        if self.email == "":
            #run search
            if "@" in userString:
                if ".co.uk" in userString.lower() or ".com" in userString.lower(): #add a for domainlist instead
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


    def checkForPhoneNumber(self, userString):
        if len(userString) == 11: 
            for char in userString:
                try:
                    char = eval(char)
                except NameError: 
                    return False
                if isinstance(char, int):
                    pass
                else:
                    return False
            return True
        else:
            return False

    def checkForWebsite(self, userString):
        domainList = [".org", ".org.uk", ".co.uk", ".com", ".gov", ".co", ".uk"] #add more

        if userString[:4].lower() == "www.":
            return True
        else:
            for domain in domainList:
                if domain in userString.lower():
                    return True
        
        return False


    def checkForCost(self, userString):
        if not self.cost:
            currencySymbols = ["£", "$"] #complete
            for symbol in currencySymbols:
                if symbol in userString:
                    return True
                else:
                    return False
        else:
            return False


    def setDeadline(self, deadline):
        self.deadline = deadline

    #Task based functions

    def completed(self):
        self.noteCompleted = True

    def incomplete(self):
        self.noteCompleted = False

    def linkTask(self, task):
        self.linkedTask = task

    def removeLinkedTask(self):
        self.linkedTask = ""

    def assignAsSubtask(self):
        self.isSubtask = True

    def unassignAsSubtask(self):
        self.isSubtask = False


    




            
                
            





        






