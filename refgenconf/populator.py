# refgenie looper plugin

import logging
import re

from ubiquerg import parse_registry_path as prp

import refgenconf

_LOGGER = logging.getLogger(__name__)


def looper_refgenie_plugin(namespaces):
    """
    A looper plugin that populates refgenie references in a PEP from
    refgenie://genome/asset:tag registry paths. This can be used to convert
    all refgenie references into their local paths at the looper stage, so the
    final paths are passed to the workflow. This way the workflow does not
    need to depend on refgenie to resolve the paths.
    This is useful for example for CWL pipelines, which are built to have
    paths resolved outside the workflow.

    :param dict namespaces: variable namespaces dict
    :return dict: sample namespace dict
    """
    rgc_path = namespaces["pipeline"]["var_templates"]["refgenie_config"]
    rgc = refgenconf.RefGenConf(rgc_path)
    return rgc.populate(namespaces)
