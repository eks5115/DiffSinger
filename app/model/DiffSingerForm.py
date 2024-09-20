from pydantic import BaseModel, Field


class Phoneme(BaseModel):
    text: str = Field()
    notes: str = Field()
    notes_duration: str = Field()
    input_type: str = Field(pattern=r'^(word|phoneme)$')


class Word(BaseModel):
    text: str = Field()
    ph_seq: str = Field()
    note_seq: str = Field()
    note_dur_seq: str = Field()
    is_slur_seq: str = Field()
    input_type: str = Field(pattern=r'^(word|phoneme)$')


class DiffSingerForm(BaseModel):
    inputs: Word | Phoneme
