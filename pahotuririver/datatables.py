from sqlalchemy.orm import joinedload
from clld.web import datatables
from clld.web.datatables.base import LinkCol, Col, LinkToMapCol
from clld.db.models import common
from clld_audio_plugin.datatables import AudioCol

from pahotuririver import models

class Words(datatables.Values):
    def col_defs(self):
        res = []
        if self.language:
            res.extend([
                LinkCol(
                    self,
                    'gloss_en',
                    sTitle=self.req._('English'),
                    model_col=common.Parameter.name,
                    get_object=lambda v: v.valueset.parameter),
            ])
        elif self.parameter:
            res.extend([
                LinkCol(self, 'language', sTitle=self.req._('Language'), get_object=lambda v: v.valueset.language),
                Col(self,
                    'desc',
                    sTitle=self.req._('Location'),
                    get_object=lambda v: v.valueset.language,
                    model_col=common.Language.description,
                ),
            ])
            # FIXME: link to map!
        res.append(Col(self, 'name', sTitle=self.req._('Word')))
        res.append(AudioCol(self, '#'))
        return res


def includeme(config):
    """register custom datatables"""
    config.register_datatable('values', Words)
