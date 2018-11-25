from numpyGCN import *


# coordinate list sparse matrix for normalized adjacency matrix
def normalize_adj(adj):
    """Symmetrically normalize adjacency matrix."""
    adj = sp.coo_matrix(adj)
    rowsum = np.array(adj.sum(1))
    d_inv_sqrt = np.power(rowsum, -0.5).flatten()
    d_inv_sqrt[np.isinf(d_inv_sqrt)] = 0.
    d_mat_inv_sqrt = sp.diags(d_inv_sqrt)
    return adj.dot(d_mat_inv_sqrt).transpose().dot(d_mat_inv_sqrt).tocoo()

def train_with_gd(model, features, adj, y_train, y_val, train_mask, val_mask, lr=0.005, epochs=100):
	losses = []
	for epoch in range(epochs):
		train_loss = model.calc_loss(features, y_train, train_mask)
		val_loss = model.calc_loss(features, y_val, val_mask)
		time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print("%s: Train/Valid Loss after epoch=%d: %f :: %f" % (time, epoch, train_loss, val_loss))
		model.gd_update(X,Y,lr)


if __name__ == '__main__':
	adj, features, y_train, y_val, y_test, train_mask, val_mask, test_mask = load_data('Cora')
	adj = normalize_adj(adj)

	# model = numpyGCN(input_dim=features.shape[1], hidden_dim=16, output_dim=y_train.shape[1])
	# train_with_gd(model, features, adj, y_train, y_val, train_mask, val_mask)

	# test_loss = model.calc_loss(features, y_test, test_mask)
	# print("Test Loss : %f" % test_loss)


