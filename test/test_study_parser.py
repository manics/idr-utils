#!/usr/bin/env python

from pyidr.study_parser import StudyParser
import pytest


class TestDOI(object):

    def test_missing_key(self):
        assert StudyParser.parse_data_doi({}, 'Study DOI') == {}

    @pytest.mark.parametrize('doi', (
        'https://doi.org/10.17867/10000134',
        'https://dx.doi.org/10.17867/10000134',
        'http://doi.org/10.17867/10000134',
        'http://dx.doi.org/10.17867/10000134'))
    def test_valid_doi_link(self, doi):
        d = {'Study DOI': doi}
        assert StudyParser.parse_data_doi(d, 'Study DOI') == {
            'Data DOI': '10.17867/10000134'}

    def test_invalid_doi_link(self):
        d = {'Study DOI': 'doi.org/10.17867/10000134'}
        with pytest.raises(Exception):
            StudyParser.parse_data_doi(d, 'Study DOI')

    def test_doi_name(self):
        d = {'Study DOI': '10.17867/10000134'}
        with pytest.raises(Exception):
            StudyParser.parse_data_doi(d, 'Study DOI')
