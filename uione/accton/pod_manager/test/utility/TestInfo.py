import csv
import xlrd
import pandas as pd

class TestInfo():
    def __init__(self):
        self.test_info_list = []
        with open('../../data/test_job.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.test_info_list.append(row)

        index_count = 4330        

        with open('../../data/SONiC_Ansible.csv', newline='') as sonic_ansible_file :
            reader = csv.DictReader(sonic_ansible_file)
            for row in reader :
                TestID = row["Test Case"]
                ansible_type = row["Topology"]
                category = row["Test Name"]
                self.test_info_list.append({"Index":index_count, \
                                            "Platform":"SONiC", \
                                            "Topo-type":"T_SONiC_Ansible", \
                                            "TestID":TestID , \
                                            "ansible_type":ansible_type , \
                                            "Model":"", \
                                            "Category":category, \
                                            'Comment':''})
                index_count += 1

        # xl = pd.ExcelFile('../../data/ansible.xlsx')
        # df1 = xl.parse('SONiC.HEAD.7-602204f')
        # ansible_type_list = ['vms-t0','vms-t1','vms-t1-lag','ptf1-32']
        # for i in range(0,len(df1)):
        #     for y in range(0,len(ansible_type_list)):
        #         self.test_info_list.append({"Index":index_count, \
        #                                     "Platform":"SONiC", \
        #                                     "Topo-type":"T_SONiC_Ansible", \
        #                                     "TestID":df1['Test Case'][i], \
        #                                     "ansible_type":ansible_type_list[y], \
        #                                     "Description":df1['Headline'][i], \
        #                                     "Category":df1['Headline'][i].split(':')[1].split(' ')[1]})
        #         index_count += 1

        with open('../../data/FB_minipack.csv', newline='') as sonic_ansible_file :
            reader = csv.DictReader(sonic_ansible_file)
            for row in reader :
                TestID = row["Test ID"]
                description = row["Description"]
                component = row["Component"]
                model = row['Model']
                comment = '-' + row['test_time'] + ' ' + row['test_type'] + ' ' +  row['stress_able'] + ' ' + row['test_utility'] + ' ' + row['description']
                self.test_info_list.append({"Index":index_count, \
                                            "Platform":"Facebook", \
                                            "Topo-type":"Minipack", \
                                            "TestID":TestID, \
                                            "Category":component, \
                                            "Model":model, \
                                            "Description":description, \
                                            'Comment':comment})
                index_count += 1

        # self.test_info_list.append({"Index":index_count, \
        #             "Platform":"SONiC", \
        #             "Topo-type":"Topology_1", \
        #             "TestID":"777", \
        #             "ansible_type":'888', \
        #             "Description":'999', \
        #             "Category":'1000'})

        self.topo_config_list = []
        with open('../../data/topology.csv', newline='') as topo_config:
            reader = csv.DictReader(topo_config)
            for row in reader:
                project = row['Project']
                topo    = row['Topology']
                model   = row['Model']
                level_1 = row['Level_1']
                level_2 = row['Level_2']
                level_3 = row['Level_3']
                level_4 = row['Level_4']
                level_5 = row['Level_5']
                self.topo_config_list.append({
                    'project': project, \
                    'topo': topo, \
                    'model': model, \
                    'level_1': level_1, \
                    'level_2': level_2, \
                    'level_3': level_3, \
                    'level_4': level_4, \
                    'level_5': level_5, \
                })
    
    def get_topo_config_by_project_and_topo(self, project, topo):
        for i in self.topo_config_list:
            if i['project'] == project and i['topo'] == topo:
                return i
        
        # return i if i['project'] == project and i['topo'] == topo for i in self.topo_config_list

    def get_topo_models(self):
        model_list = []
        for i in self.topo_config_list:
            if i['topo'] != 'Data Center Core':
                model_list.append(i['model'])
        return list(set(model_list))
    
    def get_model_config(self, model):
        for i in self.topo_config_list:
            if i['model'] == model:
                return i

    def get_by_topo_platform(self,topology,platform,model):
        data_list = []
        for row in self.test_info_list:
            if(platform == "SONiC"):
                if(row["Topo-type"] == topology and row["Platform"] == platform):
                    data_list.append({"testId":row["TestID"] + "--" +row["ansible_type"],"category":row["Category"],'comment':row['Comment']})
            elif(platform == "Facebook"):
                if(row["Topo-type"] == topology and row["Platform"] == platform and row['Model'] == model):
                    data_list.append({"testId":row["Description"],"category":row["Category"],'comment':row['Comment']})
            else:
                data_list.append({"testId":row["TestID"],"category":row["Category"],'comment':row['Comment']})
        return data_list
    
    def get_by_testId(self,testId,platform):
        data_list = []
        for row in self.test_info_list:
            if(platform != "SONiC"):
                if(row["TestID"] == testId):
                    data_list.append({"topology":row["Topo-type"],"category":row["Category"]})
            else:
                if(row["TestID"] == testId.split('/')[1]):
                    data_list.append({"topology":row["Topo-type"],"category":row["Category"]})
        return data_list