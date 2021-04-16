from playsound import playsound

class InstrumentPlayer:

       def __init__(self, notes = None, song = None, instrument = None):
             
              self.instrument = instrument
              self.folder = str(self.instrument) + '_notes'
              self.notes = notes
              self.song = song
              self.note_paths = {}
              
       def get_path(self, notes = None, Folder = None):

              if notes != self.notes and Folder != self.folder and notes != None and Folder != None:
       
                     for note in notes:
                            
                            path = folder + '/' + str(note) + '.wav'
              
                            self.note_paths[note] = path
       
              else:
                     

                     for note in self.notes:
                     
                            path = self.folder + '/' + str(note) + '.wav'
       
                            self.note_paths[note] = path
                            
                     return self.note_paths

              return self.note_paths
       
       def play_song(self, song = None, note_paths = None):
              
                     if song != self.song and note_paths != self.note_paths and song != None and note_paths != None:
                            
                            for note in song:
                                   
                                   note_to_play = note_paths[note]
                                   print(note + ' : ' + note_to_play)
                                   playsound(note_to_play)
                            
                     else:
                            
                            for note in self.song:
                                   
                                   self.note_to_play = self.note_paths[note]
                                   print(note + ' : ' + self.note_to_play)
                                   playsound(self.note_to_play)


piano_notes = ['A#', 'A', 'B', 'Bb', 'C#', 'C', 'D#', 'D', 'E', 'Eb', 'F#', 'F', 'G#', 'G']

hot_cross_buns = ['E', 'D', 'C', 'E', 'D', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'E', 'D', 'C']

piano_player = music_Player(piano_notes, hot_cross_buns, 'piano')

piano_player.get_path()

piano_player.play_song()


