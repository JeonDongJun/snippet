# jupyter에서 한 cell 저장하는 법
data, metadata = get_ipython().display_formatter.format(obj)
with open('table.html', 'w') as f:
    f.write(data['image/svg+xml'])  # Assuming the object has an HTML representation


# jupyter magic

# gpu option
%env CUDA_VISIBLE_DEVICES=1
!echo $CUDA_VISIBLE_DEVICES