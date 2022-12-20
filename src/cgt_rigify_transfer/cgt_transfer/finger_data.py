

class FingerData:
    def __init__(self):
        self.source = {
            0:  'wrist', 1: 'thumb_cmc', 2: 'thumb_mcp', 3: 'thumb_ip', 4: 'thumb_tip', 5: 'index_finger_mcp',
            6:  'index_finger_pip', 7: 'index_finger_dip', 8: 'index_finger_tip', 9: 'middle_finger_mcp',
            10: 'middle_finger_pip', 11: 'middle_finger_dip', 12: 'middle_finger_tip', 13: 'ring_finger_mcp',
            14: 'ring_finger_pip', 15: 'ring_finger_dip', 16: 'ring_finger_tip', 17: 'pinky_mcp', 18: 'pinky_pip',
            19: 'pinky_dip', 20: 'pinky_tip'
        }
        self.drivers = {name: f"driver_{name}" for k, name in self.source.items()}
        self.constraint_targets = {
            "wrist":      "hand_ik",
            "thumb_cmc":  "thumb.01",
            "thumb_mcp":  "thumb.02",
            "thumb_ip":   "thumb.03",
            "index_mcp":  "f_index.01",
            "index_pip":  "f_index.02",
            "index_dip":  "f_index.03",
            "middle_mcp": "f_middle.01",
            "middle_pip": "f_middle.02",
            "middle_dip": "f_middle.03",
            "ring_mcp":   "f_ring.01",
            "ring_pip":   "f_ring.02",
            "ring_dip":   "f_ring.03",
            "pinky_mcp":  "f_pinky.01",
            "pinky_pip":  "f_pinky.02",
            "pinky_dip":  "f_pinky.03",
        }

        self.bone_constraints = {
            'wrist': {
                'COPY_LOCATION': {
                    'target': 'wrist', 'influence': 1.0, 'owner_space': 'POSE'}},
            'thumb_cmc': {
                'COPY_LOCATION': {
                    'target': 'thumb_cmc', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.261, 'max_x': 3.14159, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'thumb_mcp': {
                'COPY_LOCATION': {'target': 'thumb_mcp', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.261, 'max_x': 3.1415926, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'thumb_ip': {
                'COPY_LOCATION': {'target': 'thumb_ip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.349, 'max_x': 3.1415926, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'index_mcp': {
                'COPY_LOCATION': {'target': 'index_mcp', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.261, 'max_x': 1.22634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'index_pip': {
                'COPY_LOCATION': {'target': 'index_pip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'index_dip': {
                'COPY_LOCATION': {'target': 'index_dip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'middle_mcp': {
                'COPY_LOCATION': {'target': 'middle_mcp', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.349, 'max_x': 1.22634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'middle_pip': {
                'COPY_LOCATION': {'target': 'middle_pip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'middle_dip': {
                 'COPY_LOCATION': {'target': 'middle_dip', 'influence': 1.0, 'owner_space': 'POSE'},
                 'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'ring_mcp': {
                'COPY_LOCATION': {'target': 'ring_mcp', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.436, 'max_x': 1.22634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'ring_pip': {
                'COPY_LOCATION': {'target': 'ring_pip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'ring_dip': {
                'COPY_LOCATION': {'target': 'ring_dip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'pinky_mcp': {
                'COPY_LOCATION': {'target': 'pinky_mcp', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.698, 'max_x': 1.22634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'pinky_pip': {
                'COPY_LOCATION': {'target': 'pinky_pip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}},
            'pinky_dip': {
                'COPY_LOCATION': {'target': 'pinky_dip', 'influence': 1.0, 'owner_space': 'POSE'},
                'LIMIT_ROTATION': {'use_limit_x': True, 'min_x': -0.136, 'max_x': 1.3962634, 'influence': 1.0, 'owner_space': 'LOCAL'}}}

        self.driver_properties = {
            'thumb_cmc': {
                'xAngle': {
                    'xAngleInput': [0.011, 0.63],
                    'xAngleOutput': [-0.6, 0.63]},
                'zAngle': {
                    'zAngleInput': [0.3491, 1.0472],
                    'zAngleOutput': [-0.4363, 0.4363]}},
            'thumb_mcp': {
                'xAngle': {
                    'xAngleInput': [0.01, 0.536],
                    'xAngleOutput': [-0.3, 0.54]}},
            'thumb_ip': {
                'xAngle': {
                    'xAngleInput': [0.008, 1.035],
                    'xAngleOutput': [-0.15, 1.03]}},
            'index_finger_mcp': {
                'xAngle': {
                    'xAngleInput': [0.105, 1.331],
                    'xAngleOutput': [-0.5, 1.33]},
                'zAngle': {
                    'zAngleInput': [-0.4363, 1.0472],
                    'zAngleOutput': [0.4363, -0.6981]}},
            'index_finger_pip': {
                'xAngle': {
                    'xAngleInput': [0.014, 1.858],
                    'xAngleOutput': [-0.2, 1.86]}},
            'index_finger_dip': {
                'xAngle': {
                    'xAngleInput': [0.34, 1.523],
                    'xAngleOutput': [-0.55, 1.52]}},
            'middle_finger_mcp': {
                'xAngle': {
                    'xAngleInput': [0.046, 1.326],
                    'xAngleOutput': [-0.5, 1.33]},
                'zAngle': {
                    'zAngleInput': [-0.6109, 0.6981],
                    'zAngleOutput': [0.6109, -0.4363]}},
            'middle_finger_pip': {
                'xAngle': {
                    'xAngleInput': [0.33, 1.803],
                    'xAngleOutput': [-0.3, 1.8]}},
            'middle_finger_dip': {
                'xAngle': {
                    'xAngleInput': [0.007, 1.911],
                    'xAngleOutput': [-0.15, 1.91]}},
            'ring_finger_mcp': {
                'xAngle': {
                    'xAngleInput': [0.012, 1.477],
                    'xAngleOutput': [-0.6, 1.48]},
                'zAngle': {
                    'zAngleInput': [-0.4363, 0.6981],
                    'zAngleOutput': [0.1745, -0.5236]}},
            'ring_finger_pip': {
                'xAngle': {
                    'xAngleInput': [0.244, 1.674],
                    'xAngleOutput': [-0.3, 1.67]}},
            'ring_finger_dip': {
                'xAngle': {
                    'xAngleInput': [0.021, 1.614],
                    'xAngleOutput': [-0.3, 1.61]}},
            'pinky_mcp': {
                'xAngle': {
                    'xAngleInput': [0.12, 1.322],
                    'xAngleOutput': [-0.8, 1.32]},
                'zAngle': {
                    'zAngleInput': [-0.6981, 0.8727],
                    'zAngleOutput': [0.3491, -0.5236]}},
            'pinky_pip': {
                'xAngle': {
                    'xAngleInput': [0.213, 1.584],
                    'xAngleOutput': [-0.5, 1.58]}},
            'pinky_dip': {
                'xAngle': {
                    'xAngleInput': [0.018, 1.937],
                    'xAngleOutput': [-0.3, 1.94]}}}
