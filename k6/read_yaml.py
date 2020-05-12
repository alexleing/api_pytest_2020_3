import os
import yaml



def get_yaml_data(yamlpath):
    '''获取yaml文件数据'''
    f = open(yamlpath, 'r', encoding='utf-8')

    yamldata = f.read()
    print(yamldata)

    # 把yaml文件数据转字典

    d = yaml.load(yamldata)
    # print(d['test_info_params'])
    f.close()
    return d

if __name__ == '__main__':
    curpath = os.path.dirname(os.path.realpath(__file__))
    print(curpath)
    yamlpath = os.path.join(curpath, 'update_info.yml')
    print(yamlpath)
    s = get_yaml_data(yamlpath)
    print(s)