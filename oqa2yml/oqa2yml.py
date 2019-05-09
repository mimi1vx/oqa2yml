from io import StringIO
import requests
from ruamel.yaml import YAML

# from openqa job we get json["job"]["test"] -> test name
#                        json["job"]["testresults"]::list->
#                                                  ["category"] -> category/
#                                                  only first test of cat.
#                                                  ["name"] -> /name
#                        json["job"]["settings"]::dict -> vars.json
#


class NoStreamYAML(YAML):
    def dump(self, data, **kw):
        stream = StringIO()
        super().dump(data, stream=stream, **kw)
        return stream.getvalue()


class Oqa2yml(object):
    def __init__(self, host, testid):
        self.testid = testid
        self.host = host
        # prepare YAML output format
        self.yaml = NoStreamYAML(typ="safe")
        self.yaml.default_flow_style = False
        self.yaml.explicit_end = True
        self.yaml.explicit_start = True
        self.yaml.indent(mapping=4, sequence=4, offset=2)
        self.data = {
            "name": None,
            "description": "Please write own description",
            "vars": None,
            "schedule": None,
        }

    def __call__(self):
        job = self._get_job(self.host, self.testid)
        self.data["schedule"] = self._parse_tests(job)
        self.data["name"] = job["test"]
        self.data["vars"] = job["settings"]

        print(self.yaml.dump(self.data))
        return 0

    @staticmethod
    def _get_job(host, testid):
        # TODO: catch errors
        data = requests.get(f"{host}/api/v1/jobs/{testid}/details").json()
        return data["job"]

    @staticmethod
    def _parse_tests(job):
        ret = []

        # can be omited
        category = job["testresults"][0]["category"]

        for m in job["testresults"]:
            category = m["category"] if "category" in m else category
            name = m["name"]
            ret.append(f"{category}/{name}")

        return ret
