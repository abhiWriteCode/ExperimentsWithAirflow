from connect import downloading, uploading
from client_1 import transformer_A, transformer_B
from client_2 import transformer_C, transformer_D
import finish


if __name__ == '__main__':
	downloading.download()

	transformer_A.data_transform()
	transformer_B.data_transform()
	transformer_C.data_transform()
	transformer_D.data_transform()

	uploading.upload()

	finish.exit()
