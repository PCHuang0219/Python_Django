import csv
import xlrd
import pandas as pd

class TestInfo():
    def __init__(self):
        self.test_info_list = []
        with open('./../../table/test_job.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.test_info_list.append(row)

        index_count = 4330        

        with open('./../../table/SONiC_Ansible.csv', newline='') as sonic_ansible_file :
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
                                            "Category":category})
                index_count += 1

        # xl = pd.ExcelFile('./../../table/ansible.xlsx')
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

        with open('./../../table/FB_minipack.csv', newline='') as sonic_ansible_file :
            reader = csv.DictReader(sonic_ansible_file)
            for row in reader :
                TestID = row["Test ID"]
                description = row["Description"]
                component = row["Component"]
                self.test_info_list.append({"Index":index_count, \
                                            "Platform":"Facebook", \
                                            "Topo-type":"Minipack", \
                                            "TestID":TestID, \
                                            "Category":component, \
                                            "Description":description})
                index_count += 1

        # self.test_info_list.append({"Index":index_count, \
        #             "Platform":"SONiC", \
        #             "Topo-type":"Topology_1", \
        #             "TestID":"777", \
        #             "ansible_type":'888', \
        #             "Description":'999', \
        #             "Category":'1000'})

    def get_by_topo_platform(self,topology,platform):
        data_list = []
        for row in self.test_info_list:
            if(platform == "SONiC"):
                if(row["Topo-type"] == topology and row["Platform"] == platform):
                    data_list.append({"testId":row["TestID"] + "--" +row["ansible_type"],"category":row["Category"]})
            elif(platform == "Facebook"):
                if(row["Topo-type"] == topology and row["Platform"] == platform):
                    data_list.append({"testId":row["Description"],"category":row["Category"]})
            else:
                data_list.append({"testId":row["TestID"],"category":row["Category"]})
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