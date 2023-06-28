from onnx import hub
from onnxruntime.quantization import preprocess
from onnxruntime.quantization import quantize_static
from onnxruntime.quantization.calibrate import CalibrationDataReader
from onnxruntime.quantization.onnx_quantizer import ONNXQuantizer

from loguru import logger

hub.set_dir("models")

model = "mnist"
preproc_model = "mnist_preproc.onnx"

mnist_models = hub.list_models(model=model)

logger.info(f"Found {len(mnist_models)} models for MNIST")
logger.info(f"Downloading {model}")
model_path = hub.download_model_with_test_data(model)
model_path += "/model.onnx"
logger.info(f"Downloaded to {model_path}")

preprocess.quant_pre_process(model_path, preproc_model)
# quantize_static(preproc_model, "mnist_quant.onnx", calibration_data_reader=)

ONNXQuantizer(preproc_model)