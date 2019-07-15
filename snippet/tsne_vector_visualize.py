# pytorch 모델로 벡터뽑아서
# tsne로 차원축소후
# matplotlib로 visualize

model.eval()
model.cuda()

layer = model._modules.get('label')


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
        outputs.append(i[0].data)

    # 5. Attach that function to our selected layer
    h = layer.register_forward_hook(copy_data)

    # 6. Run the model on our transformed image
    model(data, len(data))
    # 7. Detach our copy function from the layer
    h.remove()
    # 8. Return the feature vector


#     return outputs


import matplotlib.pyplot as plt

plt.figure(figsize=[8,8])
xs = x_embedded[np.where(y_true == 1)[0], 0]
ys = x_embedded[np.where(y_true == 1)[0], 1]
plt.scatter(xs,ys, c='C1', label='bad_x')
xs = x_embedded[np.where(y_true == 0)[0], 0]
ys = x_embedded[np.where(y_true == 0)[0], 1]
plt.scatter(xs,ys, c='C2', label='bad')

plt.legend()

# plt.savefig('/nfs/torch/ml_test/' + 'vector_rcnn.png')
plt.show()