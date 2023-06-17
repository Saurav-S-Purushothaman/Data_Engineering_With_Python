import apahce_beam as beam

class SplitWords(beam.DoFn):
    """
    a user defined function created for splitting the words in text according
    to the delimiter given
    """
    def __init__(self, delimiter=","):
        self.delimiter = delimiter

    def process(self, text):
        for word in text.split(self.delimiter):
            yield word

# doing a parDo transform
with beam.Pipeline() as pipeline:
    plants = (
        pipeline
        | 'Sports' >> beam.create([
        "Rugby", "Football", "Cricket"
    ])
        | 'Split words' >> beam.ParDo(SplitWords(','))
        | beam.Map(print)
    )

