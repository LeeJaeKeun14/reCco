import React from 'react';
import styled from 'styled-components';
const StarRating = ({ rating }) => {
  return (
    <StarRatingBlock>
      <StarRatingBack>★★★★★</StarRatingBack>
      <StarRatingFrontWrap>
        <StarRatingFront width={rating * 20}>★★★★★</StarRatingFront>
      </StarRatingFrontWrap>
    </StarRatingBlock>
  );
};

const StarRatingBlock = styled.div`
  position: relative;
  width: 80px;
`;
const StarRatingFrontWrap = styled.div`
  width: 80px;
  height: 16px;
`;
const StarRatingFront = styled.div`
  position: absolute;
  width: ${(props) => props.width}%;
  overflow: hidden;
  height: 16px;
  color: ${(props) => props.theme.color.yellow1};
  font-size: 16px;
`;
const StarRatingBack = styled.div`
  position: absolute;
  width: 80px;
  font-size: 16px;
  height: 16px;
  color: ${(props) => props.theme.color.lightGray1};
`;

export default StarRating;
