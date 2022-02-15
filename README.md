# python_bidi_multimap
python library of bi-directional multimap

# usage

## init

        d = BiMMap()

## add_pair
      
        src = [('A', {1,2,3}), ('B', {2,3,4}), ('C', {1,2,4})]
        
        for k, vs in src:
            for v in vs:
                d.add_pair(k, v)

## pair_count

        self.assertEqual(d.pair_count(), 9)
        
## keys & rkeys

        self.assertCountEqual(d.keys(), ['A', 'B', 'C'])
        self.assertCountEqual(d.rkeys(), [1,2,3,4])
        
## values & rvalues

        self.assertCountEqual(d.values(), [{1,2,3}, {2,3,4}, {1,2,4}])
        self.assertCountEqual(d.rvalues(), [{'A', 'C'}, {'A', 'B', 'C'}, {'A', 'B'}, {'B', 'C'}])

## items & ritems

        rsrc = [(1, {'A', 'C'}), (2, {'A', 'B', 'C'}), (3, {'A', 'B'}), (4, {'B', 'C'})]
        self.assertCountEqual(d.items(), src)
        self.assertCountEqual(d.ritems(), rsrc)

## iter_all_pairs & riter_all_pairs

        self.assertCountEqual(d.iter_all_pairs(), [
            ('A',1),('A',2),('A',3),('B', 2),('B', 3),('B', 4), ('C',1), ('C',2), ('C',4)
        ])
        self.assertCountEqual(d.riter_all_pairs(), [
            (1,'A'),(1,'C'),(2,'A'),(2,'B'),(2,'C'),(3,'A'),(3,'B'),(4,'B'),(4,'C')
        ])

## has_pair & rhas_pair

        self.assertTrue(d.has_pair('B', 4))
        self.assertFalse(d.has_pair('B', 1))
        self.assertTrue(d.rhas_pair(3, 'A'))
        self.assertFalse(d.rhas_pair(3, 'C'))

## get & rget

Will raise KeyError if the given key doesn't exist and no default return is provided

        self.assertRaises(KeyError, d.get, 'D')
        self.assertRaises(KeyError, d.rget, 5)
        
        self.assertEqual(d.get('D', -1), -1) # default -1
        self.assertEqual(d.get('A'), {1,2,3})
        self.assertEqual(d.rget(100, -1), -1) # default -1
        self.assertEqual(d.rget(4), {'B', 'C'})

## pop_all & rpop_all

Pop all pairs under given key, will raise KeyError if given key doesn't exist
     
        self.assertRaises(KeyError, d.pop_all, 'D')
        self.assertRaises(KeyError, d.rpop_all, 0)
        self.assertRaises(KeyError, d.pop_pair, 'A', 4)
        self.assertRaises(KeyError, d.rpop_pair, '2', 'D')
        
        d.pop_all('A')
        self.assertEqual(d.pair_count(), 6)
        d.rpop_all(1)
        self.assertEqual(d.pair_count(), 5)
        
## pop_pair & rpop_pair

Will raise KeyError if the pair is not present

        d.pop_pair('B', 2)
        self.assertEqual(d.pair_count(), 4)
        d.rpop_pair(2, 'C')
        self.assertEqual(d.pair_count(), 3)

## clear

        d.clear()
        self.assertEqual(d.pair_count(), 0)
        
