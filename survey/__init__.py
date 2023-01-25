from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Questionaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    household = models.IntegerField(label='How many people live with you in the Household', min=1, max=10)
    degree = models.StringField(
        choices=[['Highschool', 'Highschool'], ['University', 'University'], ['Vocational Training', 'Vocational Training']],
        label='What is your highest degree?',
        widget=widgets.RadioSelect,
    )
#answer = models.stringField(
    #choices=[['yes', 'yes'], ['no', 'no']],
    #label='Do you know the Nutri-Score?',
    #widget=widgets.RadioSelect,
    #)
    crt_bat = models.IntegerField(
        label='''
        How often in a week do you eat proceed food?'''
    )


    crt_lake = models.IntegerField(
        label='''
        How many categories does the Nutri-Score have?
        '''
    )

    crt_fake = models.StringField(
        label='''
            Do you know the Nutri-Score?
            '''
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['household', 'degree']


class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = ['crt_bat', 'crt_lake', 'crt_fake']


page_sequence = [Demographics, CognitiveReflectionTest]
