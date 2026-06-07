class ElectoralResult:

    def __init__(self, year, state, county, candidate, party, candidate_votes):
        '''
        Creates an electoral result with year, state, county,
        candidate, party and number of votes candidate_votes.
        '''
        self._year = year
        self._state = state
        self._county = county
        self._candidate = candidate
        self._party = party
        self._candidate_votes = candidate_votes      

    def year(self):
        ''' Returns the year of the electoral result. '''
        return self._year
    
    def state(self):
        ''' Returns the state where the election took place. '''
        return self._state
    
    def county(self):
        ''' Returns the name of the county associated with the result. '''
        return self._county

    def candidate(self):
        ''' Returns the candidate's name. '''
        return self._candidate

    def party(self):
        ''' Returns the candidate's political party. '''
        return self._party

    def candidate_votes(self):
        ''' Returns the number of votes obtained by the candidate in that county. '''
        return self._candidate_votes
    
    def __str__(self):
        ''' Returns a string representation of the result, formatted as
        [CANDIDATE@COUNTY:YEAR#VOTES] 
        '''
        return ('[' + self._candidate + '@' + self._county + ':' + str(self._year) +
                '#' + str(self._candidate_votes) + ']')
    
    def __eq__(self, other):
        ''' Compares two electoral results. Two results are considered
        equal if they share the same year, state, county and candidate.
        '''
        return (self._year == other._year and 
                self._state == other._state and
                self._county == other._county and
                self._candidate == other._candidate)

    def __lt__(self, other):
        ''' Required to allow sorting the list in state_results(state, year). '''
        return self._candidate_votes < other._candidate_votes
