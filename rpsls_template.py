#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""

import random
comp_number=random.randint(0,4)


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name=='ʯͷ':
		name=0
	elif name=='ʷ����':
		name=1
	elif name=='ֽ':
		name=2
	elif name=='����':
		name=3
	elif name=="����":
		name=4
	else:
		name=5
	return name

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��


#��дִ�д���,������ɺ�passɾ��


def number_to_name(number):
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number==0:
		number='ʯͷ'
		print("�������ѡ��Ϊ��%s" %number)
	elif number==1:
		number='ʷ����'
		print("�������ѡ��Ϊ��%s" %number)
	elif number==2:
		number='ֽ'
		print("�������ѡ��Ϊ��%s" %number)
	elif number==3:
		number='����'
		print("�������ѡ��Ϊ��%s" %number)
	else:
		number='����'
		print("�������ѡ��Ϊ��%s" %number)
	return number
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

#��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	"""
	a=name_to_number(player_choice)
	if a==comp_number:
		print("���ͼ��������һ����")
		print("����ѡ��Ϊ��%s"%choice_name)
		number_to_name(comp_number)
	elif a==5:
		print("Error: No Correct name")
	elif a==1 and comp_number in[4,0]:
		print("����ѡ��Ϊ��%s"%choice_name)
		number_to_name(comp_number)
		print("��Ӯ��")
	elif a==2 and comp_number in[1,0]:
		print("����ѡ��Ϊ��%s"%choice_name)
		number_to_name(comp_number)
		print("��Ӯ��")
	elif a==3 and comp_number in[1,2]:
		print("����ѡ��Ϊ��%s"%choice_name)
		number_to_name(comp_number)
		print("��Ӯ��")
	elif a==4 and comp_number in[2,3]:
		print("����ѡ��Ϊ��%s"%choice_name)
		number_to_name(comp_number)
		print("��Ӯ��")
	elif a==0 and comp_number in[3,4]:
		print("����ѡ��Ϊ��%s"%choice_name)
		number_to_name(comp_number)
		print("��Ӯ��")
	else:
		print("����ѡ��Ϊ��%s"%choice_name)
		number_to_name(comp_number)
		print("�����Ӯ��")
    

    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�

#����������ʾ��дִ�д��룬������ɺ�ɾ����pass


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)


