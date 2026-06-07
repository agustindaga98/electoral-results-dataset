from electoral_result import ElectoralResult

class ElectoralResultsDataset:

    def __init__(self, csv_file):
        '''
        Creates an electoral results dataset with the data
        contained in csv_file.
        '''
        # NOTE: Only the columns needed to build ElectoralResult objects
        # are read from the CSV file.
        f = open(csv_file)
        self._results = []
        f.readline()  # Skip header row
        for line in f:
            aux = line.split(',')
            r = ElectoralResult(
                int(aux[0]),  # year
                aux[1],       # state
                aux[3],       # county
                aux[6],       # candidate
                aux[7],       # party
                int(aux[8])   # candidate_votes
                )
            self._results.append(r)
        self._results.sort(reverse=True)
        f.close()
        # The sort is performed only once when building the dataset, so that
        # queries returning filtered results preserve the descending order by
        # vote count without needing to sort again. This way the sorting cost
        # is not included in each query.

    def size(self):
        '''
        Returns the number of records in the dataset. Must be O(1).
        '''
        return len(self._results)
     
    def state_results(self, state, year):
        '''
        Returns a list of electoral results for the given state and year,
        sorted in descending order by vote count.
        This operation must have O(N) time complexity.
        '''
        aux_list = []
        for result in self._results:
            if result.state() == state and result.year() == year:
                aux_list.append(result)
        return aux_list

    def votes_by_candidate(self, state, year):
        '''
        Returns a dictionary with total votes per candidate for the
        given state and year. Must be O(N * C).
        '''
        aux_dict = dict()
        aux_list = self.state_results(state, year)
        for result in aux_list:
            # If the candidate is not yet in the dictionary, add them as a new key.
            if result.candidate() not in aux_dict.keys():
                aux_dict[result.candidate()] = 0
            aux_dict[result.candidate()] = aux_dict[result.candidate()] + result.candidate_votes()
        return aux_dict

    def state_winner(self, state, year):
        '''
        Returns the candidate with the most votes in the given state and year.
        Must be O(N * C) in the worst case.
        '''
        votes = self.votes_by_candidate(state, year)
        winner = ''
        max_votes = -1  # -1 to handle the edge case of 0 votes for all candidates
        tie = 0
        tie_candidate2 = ''
        # Although the problem does not specify a particular treatment for ties
        # in state_winner, the criterion adopted is to report a tie if two
        # candidates reach the same maximum vote count.
        for candidate in votes:
            if votes[candidate] > max_votes:
                winner = candidate
                max_votes = votes[candidate]
                tie = 0
                tie_candidate2 = ''
            elif votes[candidate] == max_votes:
                tie = 1
                tie_candidate2 = candidate
        if tie == 0:
            return winner
        elif tie == 1:
            return 'TIE: ' + winner + ' ' + tie_candidate2

    def counties_won_by_party(self, year):
        '''
        Returns a dictionary with the number of counties won by each
        party in the given year.
        '''
        aux_dict = dict()       # key: party, value: win count
        counties_aux = dict()   # key: (state, county), value: [candidate_votes, party, tie_flag]
                                # tie_flag is True when there is a tie, used to avoid
                                # counting the win for any party in that county
        aux_list = []
        winning_party = ''
        for line in self._results:
            if line.year() == year:
                aux_list.append(line)
        for line in aux_list:
            county_key = line.state(), line.county()
                          # (state, county) is used to get unique combinations
            if county_key not in counties_aux:
                counties_aux[county_key] = [line.candidate_votes(), line.party(), False]
            else:
                if line.candidate_votes() > counties_aux[county_key][0]:
                    counties_aux[county_key] = [line.candidate_votes(), line.party(), False]
                elif line.candidate_votes() == counties_aux[county_key][0]:
                    counties_aux[county_key][2] = True  # Mark tie with True
        for county_key in counties_aux:
            if counties_aux[county_key][2] == False:
                winning_party = counties_aux[county_key][1]
                if winning_party not in aux_dict:
                    aux_dict[winning_party] = 0
                aux_dict[winning_party] = aux_dict[winning_party] + 1
        return aux_dict

    def export_state(self, csv_file, state):
        '''
        Generates a CSV file named csv_file containing the county-level
        electoral results for the given state.
        '''
        f = open(csv_file, 'w')
        f.write('YEAR,STATE,COUNTY,CANDIDATE,PARTY,CANDIDATE_VOTES\n')
        for result in self._results:
            if result.state() == state:
                # Numeric fields are converted to string for writing to the CSV file.
                line = (
                    str(result.year()) + ',' +
                    result.state() + ',' +
                    result.county() + ',' +
                    result.candidate() + ',' +
                    result.party() + ',' +
                    str(result.candidate_votes()) + '\n'
                    )
                f.write(line)
        f.close()
