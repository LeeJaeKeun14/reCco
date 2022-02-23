import { HYDRATE } from 'next-redux-wrapper';

const initialState = {
  loading: false,
  data: null,
  error: null,
};

export const GET_PRODUCT_INFO = 'GET_PRODUCT_INFO';
export const GET_PRODUCT_INFO_SUCCESS = 'GET_PRODUCT_INFO_SUCCESS';
export const GET_PRODUCT_INFO_FAILURE = 'GET_PRODUCT_INFO_FAILURE';

export const getProductInfoAction = (id, location = 'server') => ({
  type: GET_PRODUCT_INFO,
  location,
  id,
});

const productInfo = (state = initialState, action) => {
  switch (action.type) {
    case HYDRATE:
      const { productInfo } = action.payload;
      return { ...productInfo };
    case GET_PRODUCT_INFO:
      return {
        loading: true,
        data: null,
        error: null,
      };
    case GET_PRODUCT_INFO_SUCCESS:
      return {
        loading: false,
        data: action.payload,
        error: null,
      };
    case GET_PRODUCT_INFO_FAILURE:
      return {
        loading: false,
        data: null,
        error: action.error,
      };
    default:
      return state;
  }
};

export default productInfo;
