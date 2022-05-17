from Properties.Movable.character import CharacterHitBox
from InGame.Character.Player import Player

TIME = 0
COMMENDS_LIST = ("right", "left", "jump", "pick/drop")
# use to record
commends_running_now = []
commends_that_was_runs = []
FACE_LIST = ("^_^", "0o0", "O-O", ">.<", "!_!", "T_T")

class Record(Player):
    def __init__(self, character, x_start, y_start):
        import random
        n = random.randint(0, len(FACE_LIST)-1)
        Player.__init__(self, [character], FACE_LIST[n], 18)
        self.x_start = x_start
        self.y_start = y_start
        # reset location of x,y and x,y_past
        self.reset(x_start, y_start)

        self.steps = [] # step = [time signature, tagel ON/OFF a commend]
        self.steps_copy = []

        # when run the record it use to to say what commend needed to be run
        self.commend_tagel = []

    def tick(self):
        global TIME, commends_running_now, commends_that_was_runs, COMMENDS_LIST

        for commend in COMMENDS_LIST:
            if commend in commends_that_was_runs and commend not in commends_running_now:
                self.append(commend)
        TIME += 1

        # save the commend that was running
        commends_that_was_runs = commends_running_now
        commends_running_now = []

    def reset_record(self):
        global TIME, commends_running_now, commends_that_was_runs
        TIME = 0
        commends_running_now = []
        commends_that_was_runs = []
        self.reset(self.x_start, self.y_start)
        self.commend_tagel = []

    def run_record(self, commend):
        global commends_that_was_runs, commends_running_now
        if commend not in COMMENDS_LIST:
            print("invalid commend: ", commend, ", for character:", self.name)
            return False

        self.run_commend(commend)
        commends_running_now.append(commend)

        if commend not in commends_that_was_runs:
            self.append(commend)

        return True

    def append(self, commend):
        global TIME
        self.steps.append([TIME, commend])

    # finish recording of character, and save it in the clone list (num of clone)
    def finish_recording(self):
        global commends_running_now
        commends_running_now = []
        self.tick()
        
        # reverse for rewind the character
        self.steps.reverse()

    # rewind for one character, return how it move
    def rewind(self):
        if len(self.steps_copy) == 0:
            return []

        global TIME

        # continue until there is no more commends this frame
        while True:
            # break only if the next step is not in this frame
            if len(self.steps_copy) != 0:
                time, commend = self.steps_copy[-1]  # look at the top step of the list
                if time != TIME:
                    break
            else:                                    # else list is empty
                break

            # if this step is now! tagel it, and pop the step
            if time == TIME:
                # add/remove from the tagel list
                if commend in self.commend_tagel:
                    self.commend_tagel.remove(commend)
                else:
                    self.commend_tagel.append(commend)
                self.steps_copy.pop()

        # run the commends
        for commend in self.commend_tagel:
            self.run_commend(commend)

        # return how it move
        return self.commend_tagel


class TapeRecorder():
    def __init__(self):
        self.records_clones = []
        
    def insert(self, num, record):
        record.face_text = str(num+1)
        record.size_text = 22
        self.records_clones.insert(num, record)

    def update(self):
        for clone in self.records_clones:
            clone.update()

    def blit(self):
        for clone in self.records_clones:
            clone.blit()

    def rewind(self):
        for clone in self.records_clones:
            clone.rewind()

    def reset(self):
        for clone in self.records_clones:
            clone.reset(clone.x_start, clone.y_start)
            clone.commend_tagel = []
            clone.steps_copy = clone.steps.copy() # we will work on the steps_clone in order to rewind

    def true_reset(self):
        self.records_clones = []