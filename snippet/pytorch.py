# pytorch network visualize
from torchviz import make_dot

make_dot(model(torch.LongTensor([x[0]]).cuda(), 1))

# parameter count
model_parameters = filter(lambda p: p.requires_grad, model.parameters())
params = sum([np.prod(p.size()) for p in model_parameters])


# transfer
for param in model.parameters():
    param.requires_grad = False


# pytorch 모델로 벡터뽑아서
# tsne로 차원축소후
# matplotlib로 visualize
model.eval()
model.cuda()

layer = model._modules.get('label')
outputs = list()


def get_vector(data):
    # 1. Load the image with Pillow library
    #     img = Image.open(image_name)
    # 2. Create a PyTorch Variable with the transformed image
    #     t_img = Variable(normalize(to_tensor(scaler(img))).unsqueeze(0))
    # 3. Create a vector of zeros that will hold our feature vector
    #    The 'avgpool' layer has an output size of 512
    #     my_embedding = torch.zeros(200)
    # 4. Define a function that will copy the output of a layer
    def copy_data(m, i, o):
        outputs.append(i[0].data)  # m:layer, i: input data, o: output data

    # 5. Attach that function to our selected layer
    h = layer.register_forward_hook(copy_data)  # forward될 때 copy_data함수가 실행됨

    # 6. Run the model on our transformed image
    model(data)
    # 7. Detach our copy function from the layer
    h.remove()
    # 8. Return the feature vector

    return outputs


#repeat
import torch
tensor = torch.tensor([1., 2.])
tensor.repeat(4,1)
