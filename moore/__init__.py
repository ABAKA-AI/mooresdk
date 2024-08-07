# -*-coding:utf-8 -*-
import time
import requests

from .moore_data import *
from .api import *
from .utils.general import *
from .utils.cv_tools import *
from .utils.pc_tools import *
from .check.statistics import *
from .exception import *
from .const import *
from .factory.data_factory import ExportFactory, ImportFactory, VisualFactory, CheckFactory, PostProcessFactory


class Client:
    def __init__(self, AccessKey, SecretKey):
        self.AccessKey = AccessKey
        self.SecretKey = SecretKey
        self.api = API(self.AccessKey, self.SecretKey)

    def get_data(self, export_task_id: str):
        """
        get source data
        :param export_task_id: export task id
        :return: object
        """
        url = f"{MOORE_SDK_BASE_URL}/export/find-info"
        timestamp = int(time.time())
        payload = {
            "ak": self.AccessKey,
            "timestamp": timestamp,
            "export_task_id": export_task_id
        }

        headers = {
            'Authorization': self.api.signature_auth_task(timestamp, export_task_id),
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

        json_data = json.loads(response.text)
        if 'code' in json_data and json_data['code'] == 200:
            return json_data['data']
        else:
            raise Exception(json_data['message'])


class Export(object):
    export_f = ExportFactory()

    @classmethod
    def moore_json2coco(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_coco_product(source_data, out_path, mapping).moore_json2coco()

    @classmethod
    def sam_json2coco(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_coco_product(source_data, out_path, mapping).sam_json2coco()

    @classmethod
    def sam_json2coco_cover(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_coco_product(source_data, out_path, mapping).sam_json2coco_cover()

    @classmethod
    def moore_json2kitti(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_kitti_product(source_data, out_path, mapping).moore_json2odkitti()

    @classmethod
    def moore_json2segkitti(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_kitti_product(source_data, out_path, mapping).moore_json2segkitti()

    @classmethod
    def moore_json2labelme(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_labelme_product(source_data, out_path, mapping).moore_json2labelme()

    @classmethod
    def sam_json2labelme(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_labelme_product(source_data, out_path, mapping).sam_json2labelme()

    @classmethod
    def sam_json2labelme_cover(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_labelme_product(source_data, out_path, mapping).sam_json2labelme_cover()

    @classmethod
    def moore_json2voc(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_voc_product(source_data, out_path, mapping).moore_json2voc()

    @classmethod
    def sam_json2voc(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_voc_product(source_data, out_path, mapping).sam_json2voc()

    @classmethod
    def sam_json2voc_cover(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_voc_product(source_data, out_path, mapping).sam_json2voc_cover()

    @classmethod
    def moore_json2yolo(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_yolo_product(source_data, out_path, mapping).moore_json2yolo()

    @classmethod
    def p_mask(cls, source_data, out_path=None, mapping=None):
        cls.export_f.export_mask_product(source_data, out_path, mapping).p_mask()


class Visual(object):
    visual_f = VisualFactory()

    @classmethod
    def visual_coco(cls, source_data, data_path, out_path=None):
        cls.visual_f.visual_coco_product(source_data, data_path, out_path).visual_coco()

    @classmethod
    def visual_labelme(cls, source_data, data_path, out_path=None):
        cls.visual_f.visual_labelme_product(source_data, data_path, out_path).visual_labelme()

    @classmethod
    def visual_source(cls, source_data, out_path=None):
        cls.visual_f.visual_source_product(source_data, out_path).visual_source()

    @classmethod
    def visual_voc(cls, source_data, data_path, image_path, out_path=None):
        cls.visual_f.visual_voc_product(source_data, data_path, image_path, out_path).visual_voc()

    @classmethod
    def visual_yolo(cls, source_data, data_path, label_path, image_path, out_path=None):
        cls.visual_f.visual_yolo_product(source_data, data_path, label_path, image_path, out_path).visual_yolo()


class Check(object):
    check_f = CheckFactory()

    @classmethod
    def count_labels(cls, source_data):
        count = cls.check_f.statistics_product(source_data).count_labels()
        return count

    @classmethod
    def count_aim_labels(cls, source_data, aim_label):
        count = cls.check_f.statistics_product(source_data).count_aim_labels(aim_label)
        return count

    @classmethod
    def count_drawtype(cls, source_data, draw_type):
        count = cls.check_f.statistics_product(source_data).count_drawtype(draw_type)
        return count

    @classmethod
    def count_files(cls, source_data):
        count = cls.check_f.statistics_product(source_data).count_files()
        return count

    @classmethod
    def count_images(cls, source_data):
        count = cls.check_f.statistics_product(source_data).count_images()
        return count

    @classmethod
    def unlabeld_images(cls, source_data):
        count = cls.check_f.statistics_product(source_data).unlabeld_images()
        return count

    @classmethod
    def labeled_images(cls, source_data):
        count = cls.check_f.statistics_product(source_data).labeled_images()
        return count


class PostProcess(object):
    postprocess_f = PostProcessFactory()

    @classmethod
    def coco_split(cls, data_path, out_pat=None, test_size=0.3, train_size=None, shuffle=True):
        cls.postprocess_f.post_process_product(data_path, out_pat).split(test_size, train_size, shuffle)

    @classmethod
    def coco_merge(cls, data_path, out_pat=None, merged_file_name=None):
        cls.postprocess_f.post_process_product(data_path, out_pat).merge(merged_file_name)
