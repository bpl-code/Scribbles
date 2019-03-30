#get Progress Test

import scribbles

newTask = scribbles.task("Complete Test")
newTask.addNote(scribbles.note("Subtask 1"))
newTask.addNote(scribbles.note("Subtask 2"))
newTask.addNote(scribbles.note("Subtask 3"))
notes = newTask.getNotes()
notes[0].assignAsSubtask()
notes[1].assignAsSubtask()
print(newTask.getProgress())
