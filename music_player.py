from playsound import playsound

class music_Player:

       def __init__(self, notes , song, instrument):
             
              self.instrument = instrument
              self.folder = str(self.instrument) + '_notes'
              self.notes = notes
              self.song = song
              
       def get_path(self):

              self.note_paths = {}

              for note in self.notes:
              
                     path = self.folder + '/' + str(note) + '.wav'

                     self.note_paths[note] = path
                     
              return self.note_paths
       
       
       def play_song(self):
              
                     for note in self.song:
                            
                            self.note_to_play = self.note_paths[note]
                            print(note + ' : ' + self.note_to_play)
                            playsound(self.note_to_play)


piano_notes = ['A#', 'A', 'B', 'Bb', 'C#', 'C', 'D#', 'D', 'E', 'Eb', 'F#', 'F', 'G#', 'G']

hot_cross_buns = ['E', 'D', 'C', 'E', 'D', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'D', 'C']

piano_player = music_Player(piano_notes, hot_cross_buns, 'piano')

piano_player.get_path()

piano_player.play_song()


